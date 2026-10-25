"""DT073: đồ thị vô hướng đơn, đỉnh 1..n, DFS đệ quy."""
def tao_ke(n, canh):
    if type(n) is not int or not 1 <= n <= 100:
        raise ValueError('n phải là số nguyên từ 1 đến 100')
    if not isinstance(canh, (list, tuple)):
        raise ValueError('canh phải là danh sách cặp đỉnh')
    ke = [[] for _ in range(n + 1)]  # Bỏ trống chỉ số 0.
    da_co = set()
    for e in canh:
        if not isinstance(e, (list, tuple)) or len(e) != 2:
            raise ValueError('mỗi cạnh phải có đúng hai đỉnh')
        u, v = e
        if any(type(x) is not int or not 1 <= x <= n for x in (u, v)):
            raise ValueError('đỉnh của cạnh phải thuộc 1..n')
        if u == v:
            raise ValueError('đồ thị đơn không có khuyên')
        khoa = (min(u, v), max(u, v))
        if khoa in da_co:
            raise ValueError('đồ thị đơn không có cạnh trùng')
        da_co.add(khoa)
        ke[u].append(v)
        ke[v].append(u)
    for ds in ke:
        ds.sort()
    return ke


def dfs(ke, u, visited, kq, cha, dem, vet=None, sau=1):
    """Hàm nội bộ: chỉ gọi trên u chưa thăm, ke do tao_ke tạo."""
    visited[u] = True
    kq.append(u)
    dem['so_dinh_tham'] += 1
    dem['do_sau'] = max(dem['do_sau'], sau)
    if vet is not None:
        vet.append(f"VAO {u}: thu_tu={kq}, visited={visited[1:]}")
    for v in ke[u]:
        dem['so_lang_gien_xet'] += 1
        if not visited[v]:
            cha[v] = u
            if vet is not None:
                vet.append(f"DI {u}->{v}")
            dfs(ke, v, visited, kq, cha, dem, vet, sau + 1)
        elif vet is not None:
            vet.append(f"BO {u}->{v}: da tham")
    if vet is not None:
        vet.append(f"RA {u}")


def chay_dfs(ke, s, *, lan_vet=False):
    """ke là danh sách kề chuẩn từ tao_ke; s hợp lệ. Mỗi lần chạy reset."""
    n = len(ke) - 1
    if type(s) is not int or not 1 <= s <= n:
        raise ValueError('nguồn s phải thuộc 1..n')
    visited = [False] * (n + 1)
    cha = [0] * (n + 1)  # Nguồn/đỉnh chưa tới có cha=0; dùng visited phân biệt.
    kq = []
    dem = {'so_dinh_tham': 0, 'so_lang_gien_xet': 0, 'do_sau': 0}
    vet = [] if lan_vet else None
    dfs(ke, s, visited, kq, cha, dem, vet)
    return {'thu_tu': kq, 'visited': visited[1:], 'cha': cha[1:],
            'dem': dem, 'vet': vet or []}
