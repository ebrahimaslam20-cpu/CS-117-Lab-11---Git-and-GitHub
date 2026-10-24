 # This Aslem 
def estimate_storage():
    print("=== Storage Estimator ===")

    try:
        number_of_files = int(input("Enter the number of files: "))
        size_per_file_mb = float(input("Enter the average size of each file in MB: "))

        if number_of_files < 0 or size_per_file_mb < 0:
            print("Please enter non-negative values.")
            return

        total_mb = number_of_files * size_per_file_mb
        total_kb = total_mb * 1024
        total_gb = total_mb / 1024
        print("\n--- Storage Estimate ---")
        print(f"Number of files: {number_of_files}")
        print(f"Average file size: {size_per_file_mb:.2f} MB")
        print(f"Total storage: {total_mb:.2f} MB")
        print(f"Total storage: {total_kb:.2f} KB")
        print(f"Total storage: {total_gb:.4f} GB")
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    estimate_storage()
