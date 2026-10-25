# DT073 Duyệt đồ thị theo chiều sâu bằng đệ quy

Lê Hoàng Đức Thịnh — N24DCDT088 — D24CQDT01-N — INT13185 nhóm 03.
Giảng viên: Hồ Nhựt Minh.

## Yêu cầu và cách chạy trên Windows
Python 3.11.15, chỉ dùng thư viện chuẩn. Không cần pip install.
Mở VS Code tại thư mục chứa demo.py, mở Terminal PowerShell.
```powershell
py -3 --version
py -3 demo.py --example 1
py -3 demo.py --example 2
py -3 demo.py
py -3 test/run_tests.py --out docs/ket_qua_kiem_tra/kiem_thu_may_ca_nhan.json
py -3 survey.py
```
Nếu máy không có lệnh py nhưng có Python 3, thay `py -3` bằng `python`.
Linux/macOS dùng `python3`. Nhập mới bằng bàn phím với `demo.py` không đối số.
Ví dụ 1 có thể thêm `--trace` để in vào/ra và quay lui.

## Tổ chức
- src/dfs.py: thuật toán chính, kiểm tra đầu vào và bộ đếm.
- demo.py: ví dụ, nhập bàn phím, chạy ca chọn bằng --case.
- test/cases.json: 22 ca, input, expected và mục tiêu đặt trước khi chạy.
- test/run_tests.py: kiểm thử bằng kỳ vọng trực tiếp, bất biến và đối chứng độc lập.
- survey.py: khảo sát ba quy mô hợp lệ.
- docs/ket_qua_kiem_tra/: kết quả kiểm thử, lần vết và khảo sát.
- docs/anh_ket_qua/: nơi đặt A01.png đến A11.png sau khi chụp.

## Hợp đồng và phần tự cài
Input đồ thị vô hướng đơn, n thuộc 1..100, nguồn s thuộc 1..n. Các cạnh có đủ hai đỉnh nguyên; từ chối khuyên, cạnh trùng/đảo chiều và đỉnh ngoài miền. Mảng kề dùng chỉ số 1..n; ô 0 không dùng. `chay_dfs` nhận danh sách kề do `tao_ke` tạo; không gọi trực tiếp bằng dữ liệu kề chưa xác thực.
Tự cài DFS đệ quy và visited; danh sách kề được sort trước. Output thứ tự DFS, visited cho đỉnh 1..n, mảng cha và bộ đếm. Cha của nguồn và đỉnh chưa tới đều 0; dùng visited để phân biệt. DFS chỉ đi phần liên thông chứa nguồn. Chi phí lõi O(n+m), cộng chi phí sắp danh sách kề; tắt trace khi khảo sát.


## Tài liệu tham khảo
Phiếu giao đề tài cá nhân, giáo trình INT1306 và hướng dẫn học phần INT13185 nhóm 03 do giảng viên cung cấp ngày 17/10/2026.
