# 1 
# Special method có gì khác so với các phương thức thông thường?

# Trả lời:
# Special method là những phương thức có sẵn, chúng thường được đặt tên sẵn như __init__, __repr__,... Special method như một cái khuôn
# có sẵn và mình tự đúc "bánh" cho chiếc khuôn đó. Khác với các phương thức thông thường khác, chúng ta phải tự code để tạo ra một
# cái gì đó. Trong khi special method đã tự code sẵn cho chúng ta rồi, việc mình cần làm là nhập những số liệu của chúng ta vào thôi

# 2
# Giả sử ta cần định nghĩa hai lớp Motorbike và Car, đại diện cho các thông số và hoạt động của Xe máy và Xe hơi. Có nên áp dụng tính
# kế thừa trong quá trình định nghĩa hai lớp này không? Nếu không, vì sao? Nếu có, nêu lý do và cách tổ chức quan hệ giữa hai lớp.

# Trả lời:
# Em nghĩ là ta nên dùng tính kế thừa trong quá trình định nghĩa vì bản chất của quá trình định nghĩa hai lớp Xe máy và Xe hơi đều
# giống nhau, đều có mục thông số và hoạt động của hai loại xe. Cách tổ chức quan hệ giữa hai lớp là đầu tiên trong lớp xe máy tạo ra
# hai phương thức cho thông số và hoạt động, rồi sau đó lớp Xe hơi sẽ kế thừa hai phương thức đó của lớp Xe máy.

# 3
# B

# 4
# A

# 5
# C