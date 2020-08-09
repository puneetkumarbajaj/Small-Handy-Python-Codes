def computepay(h,r):
    if h > 40:
    	h1 = h - 40
    	pay = (40 * r) + (h1 * 1.5 * r)
    	return pay
    else:
        pay = (h * r)
        return pay

hrs = float(input("Enter Hours:"))
r = float(input("Rate:"))
p = computepay(hrs, r)
print("Pay",p)
