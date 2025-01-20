from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator


# 1. Membuat sesi Spark
spark = SparkSession.builder.appName("Personalized Recommendation System").getOrCreate()

# 2. Memuat dataset
dataset_path = "User_Purchase_and_Rating.csv"  # Ganti dengan path dataset Anda
df_large = spark.read.csv(dataset_path, header=True, inferSchema=True).dropna().dropDuplicates()

# 3. Encoding kolom "Product_Name" dan "Farm_Name" ke indeks numerik
from pyspark.ml.feature import StringIndexer
product_indexer = StringIndexer(inputCol="Product_Name", outputCol="Product_ID")
farm_indexer = StringIndexer(inputCol="Farm_Name", outputCol="Farm_ID")

# Terapkan encoding
product_indexed = product_indexer.fit(df_large).transform(df_large)
farm_indexed = farm_indexer.fit(product_indexed).transform(product_indexed)

# Pastikan kolom Product_ID dan Farm_ID ada
encoded_df = farm_indexed.select("User_ID", "Product_Name", "Farm_Name", "Rating", "Product_ID", "Farm_ID")

# 4. Dataset untuk ALS
als_data = encoded_df.select(
    col("User_ID").cast("integer"),
    col("Product_ID").cast("integer"),
    col("Rating").cast("float")
).cache()

# 5. Split data menjadi pelatihan dan pengujian
train, test = als_data.randomSplit([0.8, 0.2], seed=42)

# 6. Melatih model ALS
als = ALS(
    userCol="User_ID",
    itemCol="Product_ID",
    ratingCol="Rating",
    coldStartStrategy="drop"
)
model = als.fit(train)

# 7. Evaluasi model (RMSE)
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="Rating",
    predictionCol="prediction"
)
predictions = model.transform(test)  # Memprediksi data pengujian
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Square Error (RMSE) pada data pengujian: {rmse:.4f}")

# 8. Tentukan user yang akan diberikan rekomendasi
target_user_id = 1  # Ganti dengan ID user yang diinginkan

# 9. Ambil riwayat pembelian user
user_history = encoded_df.filter(col("User_ID") == target_user_id).select("Product_ID", "Farm_ID").distinct()

# 10. Berikan rekomendasi khusus untuk user
user_recommendations = model.recommendForUserSubset(
    spark.createDataFrame([(target_user_id,)], ["User_ID"]),
    numItems=5
)

# 11. Tambahkan nama produk ke rekomendasi
product_mapping = encoded_df.select("Product_ID", "Product_Name").distinct()

user_recommendations = user_recommendations.withColumn("recommendations", explode(col("recommendations")))

user_recommendations = user_recommendations.withColumn("Product_ID", col("recommendations").getItem("Product_ID")) \
    .withColumn("Rating", col("recommendations").getItem("rating")) \
    .join(product_mapping, on="Product_ID", how="left") \
    .select("User_ID", "Product_Name", "Rating", "Product_ID")

# 12. Tambahkan kombinasi farm dari data asli
product_farm_mapping = encoded_df.select("Product_ID", "Farm_ID", "Farm_Name").distinct()

final_recommendations = user_recommendations.join(
    product_farm_mapping,
    on="Product_ID",
    how="inner"  # Menambahkan farm ke produk
)

# 13. Filter kombinasi unik (produk + farm)
final_recommendations = final_recommendations.join(
    user_history,
    on=["Product_ID", "Farm_ID"],
    how="left_anti"  # Hanya rekomendasi produk dan farm yang belum ada di riwayat
)

# 14. Menampilkan hasil rekomendasi
print(f"Rekomendasi untuk User ID {target_user_id}:")
final_recommendations.show(truncate=False)

# 15. Menyimpan hasil rekomendasi untuk user
final_recommendations.write.parquet(f"user_{target_user_id}_recommendations2.parquet", compression="snappy")