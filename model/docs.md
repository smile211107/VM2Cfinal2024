## 2.2.1

$$

\\ 1 \le i \le 10, 1 \le j \le 200 \\
C = 1000 \\
x_{ij}: \text{số sản phẩm từ nhà máy {i} đến cửa hàng {j}}
\\
c_{i}: \text{chọn nhà máy thứ {i}}
\\
\forall i, \sum{x_{ij}} \le C * c_{i} \  \forall j \\
\forall j, \sum{x_{ij}} = D_j \ \forall i \\
\\
min(\sum{c_{i} * B_{i}} + \sum{x_{ij} * T_{ij}})
$$