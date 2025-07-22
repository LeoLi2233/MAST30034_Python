import base64
import traceback
RED = '\033[91m'
GREEN = '\033[92m'
BOLD = '\033[1m'
RESET = '\033[0m'

try:
    from pyspark.sql import SparkSession
    # Create a spark session (which will run spark jobs)
    spark = (
        SparkSession.builder.appName("MAST30034 Tutorial")
        .config("spark.sql.repl.eagerEval.enabled", True) 
        .config("spark.sql.parquet.cacheMetadata", "true")
        .config("spark.sql.session.timeZone", "Etc/UTC")
        .getOrCreate()
    )
    print(f"{GREEN}{BOLD}Success! Your environment is set up and you are ready for the first workshop.{RESET}")
except Exception as e:
    print(f"{RED}{BOLD}Something went wrong. Reinstall and try again.{RESET}")
    traceback.print_exc()