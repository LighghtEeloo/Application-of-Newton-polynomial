# -*- coding: utf8 -*-


def iterate(f, x, n):
    for k in range(n):
        ret = 0
        for i in range(len(f)):
            ret += f[i] * (x ** i)
        x = ret
    return ret


def divided_difference(lstx, lstd, n):
    len_lstx = len(lstx)
    cnt = len_lstx - n
    lstc = []
    for i in range(cnt):
        lstc.append((lstd[i] - lstd[i + 1]) / (lstx[i] - lstx[i + n]))
    return lstc


def poly_2(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    cnt = len(lst1) + len(lst2) - 1
    lst0 = [0] * cnt
    for i in range(len1):
        for j in range(len2):
            lst0[i + j] += lst1[i] * lst2[j]
    # print(lst0)

    return lst0


def poly_n(lsts):
    while len(lsts) >= 2:
        lsts[-2] = poly_2(lsts[-1], lsts[-2])
        lsts.pop()
    return lsts


def newton(lstx, lsty):
    cnt = len(lstx) - 1
    lst_di = [lsty]
    lstd = lsty
    for k in range(1, cnt + 1):
        lstd = divided_difference(lstx, lstd, k)
        lst_di.append(lstd)
    # print(lst_di)

    print()

    lst_fea = [lst[0] for lst in lst_di]
    lst_poly = [0] * len(lstx)
    lst_poly[0] += lst_fea[0]
    for k in range(len(lstx) - 1):
        lst_pol = [[-lstx[i], 1.0] for i in range(k + 1)]
        # print("lst_pol:", lst_pol)
        lst_pol = poly_n(lst_pol)[0]
        # print("pol:", lst_pol)
        for i in range(len(lst_pol)):
            # print(lst_fea[k+1], lst_pol[i])
            lst_poly[i] += (lst_fea[k + 1] * lst_pol[i])
    # print(lst_poly)
    return lst_poly


# lstx = [1, 2, 3, 4, 5]
# lsty = [0, 1, 16, 81, 256]
# print(newton(lstx, lsty))

def poly_init(poly, num_iteration):
    power = len(poly) - 1
    num_lstx = power ** num_iteration + 1
    num_start = -round(num_lstx / 2)
    lstx = [x for x in range(num_start, num_start + num_lstx)]
    lsty = []
    for x in lstx:
        lsty.append(iterate(poly, x, num_iteration))
    print("x:", lstx, "y:", lsty, sep="\n")
    return newton(lstx, lsty)


if __name__ == "__main__":
    default = 0

    if default:
        poly = [-1, 3, 1]
        num_iteration = 3
    elif not default:
        poly = [float(i) for i in input("Enter the polynomial's indeterminates, from a_0 to a_n, split by \",\" : ").split(",")]
        num_iteration = int(input("Enter the number of time to composite: "))

    print(poly_init(poly, num_iteration))
    input("Enter 0 to continue...\n")
