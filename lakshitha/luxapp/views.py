from django.shortcuts import render


def churn_rate(request):
    i = int(request.POST.get('initial', 0))
    l = int(request.POST.get('lost', 0))
    churnrate = (l / i) * 100 if request.method == 'POST' and i!=0 else 0

    print("Customers lost =", l)
    print("Total customers =", i)
    print("Churnrate =", churnrate)

    return render(request,'luxapp/churn.html', {'i': i, 'l': l, 'churnrate': churnrate}
    )
