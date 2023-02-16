from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'fm100/index.html')


def aboutfm100(request):
    return render(request, 'fm100/aboutfm100.html')


def testpage1(request):
    colorchip1 = [
        '2_ffa289.png',
        '3_ffb98d.png',
        '4_fdb27b.png',
        '5_febd6d.png',
        '6_fcc65c.png',
        '7_ffcf5c.png',
    ]
    random.shuffle(colorchip1)

    return render(request, 'fm100/tests/testphase1.html', {'color': colorchip1})


def testpage2(request):
    colorchip2 = [
        '10_cddd7a.png',
        '11_afda81.png',
        '12_9BDD86.png',
        '13_83DA93.png',
        '14_68DFA9.png',
        '15_68E0BA.png',
    ]
    random.shuffle(colorchip2)

    return render(request, 'fm100/tests/testphase2.html', {'color': colorchip2})


def testpage3(request):
    colorchip3 = [
        '18_49EEDE.png',
        '19_50E3DD.png',
        '20_64E1F7.png',
        '21_82D5F5.png',
        '22_89CCF6.png',
        '23_93C6FD.png',
    ]
    random.shuffle(colorchip3)

    return render(request, 'fm100/tests/testphase3.html', {'color': colorchip3})


def testpage4(request):
    colorchip4 = [
        '26_B7AEDD.png',
        '27_D0B0E2.png',
        '28_DFACD7.png',
        '29_EFABD4.png',
        '30_F8A6CE.png',
        '31_FFA4B3.png',
    ]
    random.shuffle(colorchip4)

    return render(request, 'fm100/tests/testphase4.html', {'color': colorchip4})



