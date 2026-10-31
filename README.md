# DT073 Duyệt đồ thị theo chiều sâu bằng đệ quy

Lê Hoàng Đức Thịnh — N24DCDT088 — D24CQDT01-N — INT13185 nhóm 03.
Giảng viên: Hồ Nhựt Minh.

## Yêu cầu và cách chạy trên Windows
Môi trường dự kiến trên máy cá nhân: Python 3.14.5; xác nhận bằng lệnh bên dưới. Chỉ dùng thư viện chuẩn. Không cần pip install.
Mở VS Code tại thư mục chứa demo.py, mở Terminal PowerShell.
```powershell
python --version
python demo.py --example 1
python demo.py --example 2
python demo.py
python test/run_tests.py --out docs/ket_qua_kiem_tra/kiem_thu_may_ca_nhan.json
python survey.py
```
Nếu máy không có lệnh py nhưng có Python 3, thay `python` bằng `python`.
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

## Đối chiếu phiên bản và minh chứng
Các kết quả trong docs/ket_qua_kiem_tra là kết quả kiểm tra khi chuẩn bị mã, không thay thế ảnh chạy cá nhân A01–A11. Chạy lại trên máy cá nhân để xác nhận phiên bản Python, lưu log và chụp ảnh. Điền SHA C/S, permalink và kết quả thực tế vào ThongTinNop.txt sau khi chốt phiên bản.

## Bằng chứng máy cá nhân và tình trạng GitHub
Log kiem_thu_may_ca_nhan.json: Python 3.14.5, 22/22 PASS, 234 phép kiểm. A09 gồm A09a.png và A09b.png. A10 hiện thể hiện clone GitHub bị lỗi thiếu src; cần cập nhật đủ cấu trúc rồi clone chạy lại. A11 và C/S chưa hoàn tất.
Thư mục src phải nằm cùng cấp với demo.py; giữ cả src/dfs.py và src/__init__.py.
