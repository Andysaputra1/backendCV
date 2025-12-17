import os

def split_file(file_path, chunk_size=90*1024*1024): # Potong per 90MB (Biar aman dibawah 100MB)
    if not os.path.exists(file_path):
        print(f"File {file_path} tidak ditemukan!")
        return

    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        part_num = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_name = f"{file_name}.part{part_num}"
            with open(part_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Dibuat bagian: {part_name}")
            part_num += 1
    print("Selesai memecah file!")

# Jalankan fungsi
split_file('best_mushroom_cnn.keras')