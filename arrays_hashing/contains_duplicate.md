# Contains Duplicate

**Link:** https://neetcode.io/problems/duplicate-integer
**Độ khó:** Easy
**Pattern:** Hash Set

## Đề bài

Cho một mảng số nguyên `nums`. Trả về `True` nếu có bất kỳ số nào xuất hiện nhiều hơn một lần, ngược lại trả về `False`.

Ví dụ:
- `nums = [1, 2, 3, 3]` → `True` (số 3 xuất hiện 2 lần)
- `nums = [1, 2, 3, 4]` → `False` (không số nào lặp lại)

## Cách tư duy

Câu hỏi cốt lõi với mỗi số là: **"số này đã từng xuất hiện chưa?"**

- **Cách ngây thơ (brute force):** với mỗi số, đi so sánh nó với tất cả số còn lại. Hai vòng lặp lồng nhau → O(n²), chậm khi mảng lớn.
- **Cách tốt hơn:** dùng một `set` để nhớ những số đã gặp. Set kiểm tra "đã có chưa" gần như tức thời — O(1). Nhờ vậy chỉ cần duyệt mảng *một lần*.

> **Pattern cần nhớ:** dùng hash set để ghi nhớ những thứ đã thấy → phát hiện trùng lặp trong một lần duyệt. Pattern này quay lại trong rất nhiều bài khác.

## Các bước

1. Tạo một set rỗng `seen` để lưu các số đã gặp.
2. Duyệt qua từng số `num` trong mảng:
   - Nếu `num` đã có trong `seen` → tìm thấy trùng → trả về `True`.
   - Nếu chưa → thêm `num` vào `seen`, đi tiếp.
3. Duyệt hết mảng mà không gặp trùng → trả về `False`.

## Độ phức tạp

- **Thời gian:** O(n) — duyệt mảng đúng một lần, mỗi thao tác kiểm tra/thêm vào set là O(1).
- **Bộ nhớ:** O(n) — trong trường hợp xấu nhất (không có số trùng), set chứa cả n phần tử.
