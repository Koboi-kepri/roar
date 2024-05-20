import asyncio
from truecallerpy import login, search_phonenumber

# Memperbaiki masalah import MutableSet
from collections.abc import MutableSet

async def main():
    # Ganti dengan nomor telepon yang ingin Anda cari
    nomor_telepon = "+6201326020530"

    try:
        # Lakukan login ke akun Truecaller (gunakan nomor telepon Anda)
        login_response = await login("+1234567890")
        print("Respons Login:", login_response)

        # Cari nomor telepon
        search_response = await search_phonenumber(nomor_telepon)
        print("Respons Pencarian:", search_response)

        # Ekstrak informasi spesifik (misalnya nama pemilik nomor telepon)
        nama_pemilik = search_response.get("name", "Tidak ditemukan")
        print(f"Pemilik nomor {nomor_telepon}: {nama_pemilik}")

        # Ekstrak informasi tambahan dari query
        jenis_nomor = search_response.get("number_type", "Tidak ditemukan")
        nomor_valid = search_response.get("valid_number", "Tidak ditemukan")
        nomor_val_ldforregion = search_response.get("val_ldforregion", "Tidak ditemukan")
        kode_negara = search_response.get("country_code", "Tidak ditemukan")
        kode_area = search_response.get("area_code", "Tidak ditemukan")
        ekstensi = search_response.get("ext", "Tidak ditemukan")
        format_e164 = search_response.get("format_e164", "Tidak ditemukan")
        format_nasional = search_response.get("format_national", "Tidak ditemukan")
        format_internasional = search_response.get("format_international", "Tidak ditemukan")
        kode_dial_dari_negara = search_response.get("dial_from_country_code", "Tidak ditemukan")
        nomor_dial_dari_negara = search_response.get("dial_from_country_number", "Tidak ditemukan")
        operator = search_response.get("carrier", "Tidak ditemukan")
        benua = search_response.get("continent", "Tidak ditemukan")
        kode_benua = search_response.get("continent_code", "Tidak ditemukan")
        kode_negara_iso = search_response.get("country", "Tidak ditemukan")
        nama_negara = search_response.get("country_name", "Tidak ditemukan")
        region = search_response.get("region", "Tidak ditemukan")
        nama_region = search_response.get("region_name", "Tidak ditemukan")
        kota = search_response.get("city", "Tidak ditemukan")
        kode_pos = search_response.get("zip", "Tidak ditemukan")
        latitude = search_response.get("lat", "Tidak ditemukan")
        longitude = search_response.get("lon", "Tidak ditemukan")
        zona_waktu = search_response.get("timezone", "Tidak ditemukan")
        offset = search_response.get("offset", "Tidak ditemukan")
        mata_uang = search_response.get("currency", "Tidak ditemukan")

        # Tampilkan informasi tambahan
        print(f"Jenis Nomor: {jenis_nomor}")
        print(f"Valid: {nomor_valid}")
        print(f"Val LdForRegion: {nomor_val_ldforregion}")
        print(f"Kode Negara: {kode_negara}")
        print(f"Kode Area: {kode_area}")
        print(f"Ekstensi: {ekstensi}")
        print(f"Format E164: {format_e164}")
        print(f"Format Nasional: {format_nasional}")
        print(f"Format Internasional: {format_internasional}")
        print(f"Kode Dial Dari Negara: {kode_dial_dari_negara}")
        print(f"Nomor Dial Dari Negara: {nomor_dial_dari_negara}")
        print(f"Operator: {operator}")
        print(f"Benua: {benua}")
        print(f"Kode Benua: {kode_benua}")
        print(f"Kode Negara ISO: {kode_negara_iso}")
        print(f"Nama Negara: {nama_negara}")
        print(f"Region: {region}")
        print(f"Nama Region: {nama_region}")
        print(f"Kota: {kota}")
        print(f"Kode Pos: {kode_pos}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Zona Waktu: {zona_waktu}")
        print(f"Offset: {offset}")
        print(f"Mata Uang: {mata_uang}")

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
