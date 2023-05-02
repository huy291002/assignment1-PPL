import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        """test 1 """
        input = """  
        a, b: integer=1,2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_2(self):
        """test 2 """
        input = """  
        a, b: array[5] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_3(self):
        """test 3 """
        input = """  
        a,b: integer = 1,2,3;
        """
        expect = "Error on line 2 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_4(self):
        """test 4 """
        input = """  
        {1_231,2,3, "Huy"}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_5(self):
        """test 5 """
        input = """  
        {true,false}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_6(self):
        """test 6 """
        input = """  
        a[i] = 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_7(self):
        """test 7 """
        input = """  
        a == 2;
        """
        expect = "Error on line 2 col 10: =="
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_8(self):
        """test 8 """
        input = """  
        a,b,c: integer=123_23,421.23,432.e3;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_array9(self):
        """test 9 """
        input = """  
        array [1_2,2_3] of integer
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_array10(self):
        """test 10 """
        input = """  
        array [1_2_23,2_3_4221] of float
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_array11(self):
        """test 11 """
        input = """  
        array [1_2_23,2_3_422.1] of float
        """
        expect = "Error on line 2 col 22: 23422.1"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_func12(self):
        """test 12 """
        input = """  
        fact : function integer(n:integer, s:string) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_13(self):
        """test 13 """
        input = """
        {
        r, s: string;
        r = 2.011;
        c, d: array [5] of integer;
        s = r * r * myPI;
        a[0] = s;
        c,d: integer = 2,9;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_14(self):
        input = """
                for (i = 1, i < 10, i + 1) {
                    writt(i);
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_15(self):
        input = """
                for (i = 1, i < 10, i + 1)
                    writeInt(i);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16(self):
        input = """
                for (i =2,i<3,i+2)
                    writeInt(i);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17(self):
        input = """
                while (huy <= 1000)
                {
                    huy = huy::huy;
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18(self):
        input = """
                do
                {
                    a = a::a;
                }
                while (che == 1);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19(self):
        input = """
                do
                {
                    b = b::b;
                    break;
                }
                while (b == 1_2910);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """
        {
        helloo(2_2910 + d, 421_21.0 / h);
        hui();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = """
                {
                r, s: integer;
                r = 3.021;
                d, e: array [5] of integer;
                a = b * b * myPI;
                a[0] = s;
                a,b,c: integer = 1,2,3;
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = """
                x: integer = 65;
                inc: function void(out n: integer, delta: integer)
                {
                n = n + delta;
                }
                inc(x, delta);
                hello(x);
                
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
        input = """
                a,c,d: integer =2,3,4;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
        input = """
                if (h == 1)
                {
                    for (d = 2, d < 30, d + 29)
                    {
                        a[d] = d;
                    }      
                } 
                else 
                {
                    do
                    {
                        hui(huy, 12);
                        b[1,2,3,4,5] = 5;
                    }while (che < 1);
                         
                } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_func25(self):
        """test 25 """
        input = """  
        fact : function auto(n:integer, s:string, a: auto) {
        if (n==2) {
            i=2;
        }
        else i = i+1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_func26(self):
        """test 26 """
        input = """  
        fact : function auto(n:integer, s:string, a: auto) inherit super {
        if (n==2) {
            i=2;
        }
        else i = i+1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_func27(self):
        """test 27 """
        input = """  
        fact : function auto(n:integer, s:string, a: auto) inherit super {
        if (n==2) {
            i=2;
        }
        else i = i+1;
        }
        inc: func int(k: string, a: integer, inherit b array){
        for (i =1, i <10, i+1){
        a=a+1;
        }
        }
        """
        expect = "Error on line 8 col 13: func"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_func28(self):
        """test 28 """
        input = """  
        fact : function auto(n:integer, s:string, a: auto) inherit super {
        if (n==2) {
            i=2;
        }
        else i = i+1;
        }
        inc: function string(k: string, a: integer, inherit b: array, inherit out f: integer){
        for (i =1, i <10, i+1){
        a=a+1;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_func29(self):
        """test 29 """
        input = """  
        fact : function auto(n:integer, s:string, a: auto, out h: auto) inherit super {
            do 
            {
            i=i+1;
            a = a+2;
            a[0,1] = s;
            }
            while (x<2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_func30(self):
        """test 30 """
        input = """  
        fact : function auto(n:integer, s:string, a: auto, out h: auto) {
            do 
            {
            i=i+1;
            a = a+2;
            a[0,1] = s;
            }
            while (x<2);
            while (x==2)
                i =i+1;
            while (--i)
            {
            i=i-2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_func31(self):
        """test 31 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
            a=1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_func32(self):
        """test 32 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
            a=1;
            for (i =2, i<2, -i)
            {
            return fact(n-1);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_func33(self):
        """test 33 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
                a=1;
                while (a==2)
                {
                    i = i+3;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_func34(self):
        """test 34 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
                if (a==1)
                    a=a+2;
                else b=a+2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_func35(self):
        """test 35 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
                return b*helo(a-1);
            else
                foo(x+2,y*2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_func36(self):
        """test 36 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
                return b*helo(a-1);
            else
                foo(x+2,y*2);
        }
        huy: func boolean(b: integer)
        {
        a=2;
        }
        """
        expect = "Error on line 10 col 13: func"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_func37(self):
        """test 37 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            if (a != 29)
                return b*helo(a-1);
            else
                foo(x+2,y*2);
        }
        huy: function boolean(b: integer)
        {
        a=2;
        }
        daddy: function integer(out a:integer, inherit b: string)
        {
        a,b,c: integer=29,10,9;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_func38(self):
        """test 38 """
        input = """  
        helo : function void(n:integer) {
            x : integer =29;
            a,b: integer=29,10;
            return foo(x*2);
            for (a = 3, a != 3, a*2)
            {
            if (a==100)
            break;
            else
            continue;
            }
        }
        huy: function boolean(b: integer)
        {
        a=2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_func39(self):
        """test 39 """
        input = """  
        helo : function void(n:integer) {
            break;
            continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_func40(self):
        """test 40 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
            foo(2*x,4*3);
            return goo(2+3)*a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_func41(self):
        """test 41 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
            foo(2*x,4*3,4.0/a);
            return goo(2+3)*a;
            }
        bye: function void(out h: string, inherit b:integer, inherit out d: auto)
        {
        if (!foo(2*3,4/x))
        a=a+2;
        else
        a=a/2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_func42(self):
        """test 42 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
            foo(2*x,4*3,4.0/a);
            return goo(2+3)*a;
            }
        bye: function void(out h: string, inherit b:integer, inherit out d: auto)
        {
        while (foo(2*3,4/x))
        a=a+2;
        }
        alo: function string(a: integer, b: string)
        {
        goo();
        foo(2*3);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_func43(self):
        """test 43 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
                a,b,c,d: integer =1,2,3,4;
                a,d: integer =2,3,4;
        }
        """
        expect = "Error on line 4 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_func44(self):
        """test 44 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
                a: integer = 25;
                a[1_1,1_2_345_2]=5;
                do
                {
                a[0] = h;
                saybye(2*2,y*3);
                if (saybye())
                return foo(n-2);
                }
                while (a <= 2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_func45(self):
        """test 45 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
                if (a >= b)
                {
                sayhello();
                }
                else
                saygoodbye(2*3);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_func46(self):
        """test 46 """
        input = """  
        goodbye : function auto(n:integer, b: string, inherit c: array) {
                if (a >= 12_234.e+2)
                {
                sayhello();
                }
                else
                saygoodbye(2*3);
                for (i =1, i<2, i+2)
                {
                    foo();
                    break;
                    return;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_func47(self):
        """test 47 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
                if (a >= b)
                {
                sayhello();
                }
                else
                saygoodbye(2*3);
                return sayhelo(2*x,x-2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_func48(self):
        """test 48 """
        input = """  
        helo : function auto(n:integer, b: string, inherit c: array) {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_func49(self):
        """test 49 """
        input = """  
        fat: function integer(a: integer)
        {
            if (2343.e+2 > d)
            {
                a =1;
            }
            else
            break;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_func50(self):
        """test 50 """
        input = """  
        fat: function integer(a: integer)
        {
            if (2343.e+2 > d)
            {
                a =1;
            }
            else
                return ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_51(self):
        """Simple program: while() {} """
        input = """
        while (huy != 0) {
            c, d: integer;
            a, h: array [9] of integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
        
    def test_52(self):
        """Simple program: while() {} """
        input = """
        while (_a != 1_2_3_29_1_0) {
            _a_b, _1: string;
            a_29, h10: array [2,9] of integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
        
    def test_53(self):
        """Simple program: while() {} """
        input = """
        while (_huy >= 1_23) {
            _c_d_29, _huy29: string;
            c_24, d_29: array [29,24,6] of integer;
            __ : integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        
    def test_54(self):
        """Simple program: while() {} """
        input = """
        while (__a_b >= 1_11_29) {
            _cd_11 : integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        
    def test_55(self):
        """Simple program: while() {} """
        input = """
        while (__huy == 1_2) {
            che : string;
            d: integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
        
    def test_56(self):
        """Simple program: do() {} """
        input = """
        do {
            _lam = 1_2 + 34_0;
            huy = i::a;
        } while (huy != 1_2_3_2910);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
        
    def test_57(self):
        """Simple program: do() {} """
        input = """
        do {
            d, t: string;
            d = 1_6_29_1;
            huy = a + 12.e-1;
        } while (ba == _huy);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
        
    def test_58(self):
        """Simple program: do() {} """
        input = """
        do {
            a, b: float;
            a = 1_7;
            c = d + 12.e-1;
        } while (d + 2);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
        
    def test_59(self):
        """Simple program: do() {} """
        input = """
        do {
            c, d: integer;
            f = 1_6.E-2;
            h = (a-2) + 12.e-1;
        } while ((_huy*1_2_29) + 2);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
        
    def test_60(self):
        """Simple program: do() {} """
        input = """
        do {
            d, a: integer = 1+2,(2* (3_2 + 1_00));
            huy = (huy-2) + 12.e-1;
        } while ((_huy*1_2) != 2_1_19);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
        
    def test_61(self):
        """Simple variable"""
        input = """_huy: string = 2_29;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
        
    def test_62(self):
        """Simple variable"""
        input = """_q, a_1_29: boolean = true, 27_12_29_10;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test_63(self):
        """Simple variable"""
        input = """t , __, x: string = "quan", 1_23.e+2, 2_0;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
        
    def test_64(self):
        """Simple variable"""
        input = """huy, __: string = "good", 1_23.e+2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        
    def test_65(self):
        """Simple variable"""
        input = """d, c: string = huy, 1_23.e+2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
        
    def test_66(self):
        """Simple variable"""
        input = """A, D, d: integer = ab, 1_23.e+2;"""
        expect = "Error on line 1 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 266))
        
    def test_67(self):
        """Simple variable"""
        input = """bcd, x: integer = bc, 1_23.e+2, x;"""
        expect = "Error on line 1 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 267))
        
    def test_68(self):
        """Simple variable"""
        input = """_h, bc: float = "string", 1_23.e+2, x;"""
        expect = "Error on line 1 col 34: ,"
        self.assertTrue(TestParser.test(input, expect, 268))
        
    def test_69(self):
        """Simple variable"""
        input = """__, bHE, a1, e_e: string = "string", 1_23.e+2, y;"""
        expect = "Error on line 1 col 48: ;"
        self.assertTrue(TestParser.test(input, expect, 269))
    
    def test_70(self):
        """Simple variable"""
        input = """aA_3, _a_3 :integer = "string", aB, 1_23;"""
        expect = "Error on line 1 col 34: ,"
        self.assertTrue(TestParser.test(input, expect, 270))
        
    def test_71(self):
        """If statement"""
        input = """
            if (huy < 0) {
                _b, aY3: integer = 1_24, "huy";
                good(a, _b, 1.2e+10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
        
    def test_72(self):
        """If statement"""
        input = """
            if (127_29_10 == "quan") {
                _ade, x2: boolean = "string", 3.e-1;
                bye(a, _b, 1.2e+10);
                shut();
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
        
    def test_73(self):
        """If statement"""
        input = """
            if (huy <= lam) {
                _huy_z, z9: array [2,3] of boolean = "string", 329.e-1;
                return;
            } else break;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
        
    def test_74(self):
        """If statement"""
        input = """
            if ((huy+29_19) >= 29_1_3.e+10) {
                che = 1;
                huy, che: array [1] of boolean = true, 123_0_29_10_12;
                continue;
            } else {
                _huy = ch + (th + quan);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        
    def test_75(self):
        """If statement"""
        input = """
            if (((2_3-1.2e-1)/2 > huy) == 29_10) {
                huy = 1_29;
                break;
            } else {
                huy = true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
        
    def test_76(self):
        """If statement"""
        input = """
            if ((_huy - quan) == 29_10) {
                x = "integer";
            } else {
                quan = 1_9_29.543;
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
        
    def test_77(self):
        """If statement"""
        input = """
            if (!huy == (2+3)*4) {
                return quan(huy, true);
            } else {
                huy();
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        
    def test_78(self):
        """If statement"""
        input = """
            if (!thanh) {
                return soo(huy, true);
            } return saka(huy, false);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test_79(self):
        """If statement"""
        input = """
            if (-arteta == 0) {
                return messi(x, true) + ronaldo(y, false);
            } return maria(x+1, false);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    def test_80(self):
        """If statement"""
        input = """
            if (-huy == (9_2 / _x)) {
                return messi(saka, true) + dimaria(arteta, false);
            } return thanh /2 ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
        
    def test_81(self):
        """If statement"""
        input = """
            {
                _bX =  messi(p, true);
                {
                    _aX = ronaldo(2, "integer");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
        
    def test_82(self):
        """If statement"""
        input = """
            {
                _bhuy =  messi(p, true);
                huy, che: integer = 1_29_10_2, 0;
                {
                    _huy = messi(2, "string");
                    return ronaldo();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
        
    def test_83(self):
        """If statement"""
        input = """
            {
                x, b: integer = 1_2, .23e10;
                arr: array [1] of  boolean = true;
                {
                    _aD = messi(2, "string");
                    return ronaldo(true);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        
    def test_84(self):
        """If statement"""
        input = """
            {
                {
                    _aD = messi(2, "string");
                    return ronaldo(false);
                    {
                        
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
        
    def test_85(self):
        """If statement"""
        input = """
            if (h_2910 != "quan") {
                d: float;
                {
                    d: string;
                }
            } else return messi(true);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
        
    def test_86(self):
        """If statement"""
        input = """
            if (q_2910 <= "quan") {
                h: integer;
                {
                    h: float; {
                        h: array [2,3] of float;
                    }
                    h = {"huy", 29};
                }
            } else return messi({1,2,3});
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        
    def test_87(self):
        """If statement"""
        input = """
            if (huy == "str") {
                huy: float;
                {
                    huy: string;
                    huy= "quan";
                }
                {
                    huy: boolean; 
                    {
                        huy: array [2,3] of float = {6,7,8,9,10};
                    }
                    huy = {"huy", 1};
                }
            } else break;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
        
    def test_88(self):
        """If statement"""
        input = """
            {
                {
                    {
                    
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
        
    def test_89(self):
        """If statement"""
        input = """
            if (huy == "") {
                {
                    return messi(false);
                    continue;
                }
            } else return ronaldo(true);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
        
    def test_90(self):
        """If statement"""
        input = """
            if (!messi(true) == "false") {
                {
                    return messi(true) + 29;
                }
            } else return huy(false) - 10;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_func91(self):
        """test 91 """
        input = """  
        for (i=10, i<2, i*2)
        {
            foo(2*x);
            if (a < 23_34)
            {
                goo();
            }
            else
            {
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_func92(self):
        """test 92 """
        input = """  
        for (i=10_234, i<2_234_3, i/2)
        {
            foo(2*y,3+t);
            if (foo(2*y,3+t))
            {
                return;
            }
            else
            {
                break;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_func92(self):
        """test 92 """
        input = """  
        for (i=10_234, i<2_234_3, i/2)
        {
            continue;
            if (a >= 232_2365)
            {
                a,d: integer = 23_45,54_57;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_func93(self):
        """test 93 """
        input = """  
        for (i=10_234, i<2_234_3, i/2)
        {
            continue;
            if (a >= 232_2365)
            {
                a,d: integer = 23_45,54_57;
            }
            else
            {
                b,c: float = 23_45e2,2342.2e4;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_func94(self):
        """test 94 """
        input = """  
        for (i=10_23_2321, i<2_234_3, i/2_1242)
        {
            if (a <= 232_2365)
            {
                foo(232_2365*x,432_29+y);
            }
            else
            {
                return fact(n-1);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_func95(self):
        """test 95 """
        input = """  
        for (i=10_23_2321, i<2_234_3, i/2_1242)
        {
            while ( a != 234_32e-2)
            {
                if (x != 2)
                {
                x=x+1;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_func96(self):
        """test 96 """
        input = """  
        for (i=10_23_2321, i<2_234_3, i/2_1242)
        {
            do
            {
                if (x<=1)
                    x=x+1;
                else
                    return fact(n*2);
            }
            while (a >= 2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_func97(self):
        """test 97 """
        input = """  
        for (i=1_234_1_294, i < 1223_2_2_42, i + 2345e+2)
        {
            return;
            break;
            continue;
            do
            {
                x = 3;
            }
            while ( x !=2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_func98(self):
        """test 98 """
        input = """  
        for (i=1_234_1_294, i < 1223_2_2_42, i + 2345e+2)
        {
            do
            {
                x = {"huy","quan", thien};
            }
            while ( x !=2);
        }
        inc: function integer(a: string, b: integer)
        {
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_func99(self):
        """test 99 """
        input = """  
        for (i=1_234_1_294, i < 1223_2_2_42, i + 2345e+2)
        {
            hello(2*x,3/y);
            bye(2+3,y/4);
        }
        inc: function void(i: integer, b: string)
        {
            return goo(2/3,24*y);
            a={1,2,3,4};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test_func300(self):
        """test 300 """
        input = """  
        for (i=1_234_1_294, i < 1223_2_2_42, i + 2345e+2)
        {
            testcase(10*2);
            if (a==2)
            {
                h,c,d: integer =123_23,1_4_8_9_0,29_1_0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
    

    
    
    
        
    
    
        
        