# DT073 Duyệt đồ thị theo chiều sâu bằng đệ quy

Lê Hoàng Đức Thịnh — N24DCDT088 — D24CQDT01-N — INT13185 nhóm 03.
Giảng viên: Hồ Nhựt Minh.

## Yêu cầu và cách chạy trên Windows
Môi trường đã chạy theo ảnh và log cá nhân: Python 3.14.5. Chỉ dùng thư viện chuẩn. Không cần pip install.
Mở VS Code tại thư mục chứa demo.py, mở Terminal PowerShell.
```powershell
python --version
python demo.py --example 1
python demo.py --example 2
python demo.py
python test/run_tests.py --out docs/ket_qua_kiem_tra/kiem_thu_may_ca_nhan.json
python survey.py
```
Nếu máy chỉ nhận lệnh `py`, có thể thay `python` bằng `py -3`.
Linux/macOS dùng `python3`. Nhập mới bằng bàn phím với `demo.py` không đối số.
Ví dụ 1 có thể thêm `--trace` để in vào/ra và quay lui.

## Tổ chức
- src/dfs.py: thuật toán chính, kiểm tra đầu vào và bộ đếm.
- demo.py: ví dụ và nhập bàn phím; --example hoặc --input cho Thịnh.
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


## Phiên bản và kết quả đã có
Ảnh A10a/A10b: clone vào Thinh_Clone_Cuoi; HEAD=0347b0a26d4137b2efe6a4a37920262f9d85091b; Python 3.14.5. VD01 có thứ tự [1,2,4,3]; VD02 có thứ tự [2,1,3]. Bộ kiểm thử đạt 22/22 PASS, 0 FAIL, 234 phép kiểm.
Ảnh A11: kho GitHub công khai, nhánh main, commit 0347b0a; thể hiện docs, inputs, src, test, README.md, demo.py và survey.py. Ảnh gốc: docs/anh_ket_qua/A11.png.

SHA C: `0347b0a26d4137b2efe6a4a37920262f9d85091b`.

- Thuật toán: https://github.com/N24DCDT088LeHoangDucThinh/N24DCDT088_DT073_LeHoangDucThinh/blob/0347b0a26d4137b2efe6a4a37920262f9d85091b/src/dfs.py
- Kiểm thử: https://github.com/N24DCDT088LeHoangDucThinh/N24DCDT088_DT073_LeHoangDucThinh/blob/0347b0a26d4137b2efe6a4a37920262f9d85091b/test/run_tests.py
