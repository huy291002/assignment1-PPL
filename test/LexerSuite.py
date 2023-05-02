import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.test('/* A C-style comment */a=5; // A C++ style comment', "a,=,5,;,<EOF>", 101))
    def test_identifiers_comment(self):
        """test identifiers_comment"""
        self.assertTrue(TestLexer.test('string a ="hello thay quan" // day la comment', "string,a,=,hello thay quan,<EOF>", 102))
    def test_identifiers_2(self):
        """test identifiers_2"""
        self.assertTrue(TestLexer.test('___abc2910 a_bchuy', "___abc2910,a_bchuy,<EOF>", 103))
    def test_identifiers_3(self):
        """test identifiers_3"""
        self.assertTrue(TestLexer.test('huy_2910 _2341huy2910.789', "huy_2910,_2341huy2910,.,789,<EOF>", 104))
    def test_identifiers_float(self):
        """test identifiers_float"""
        self.assertTrue(TestLexer.test('int a = 234_542.294e+3', "int,a,=,234542.294e+3,<EOF>", 105))
    def test_identifiers_5(self):
        """test identifiers_5"""
        self.assertTrue(TestLexer.test('abc b_123_456', "abc,b_123_456,<EOF>", 106))
    def test_identifier_6(self):
        """test identifiers_6"""
        self.assertTrue(TestLexer.test('huy_abc ___2910', "huy_abc,___2910,<EOF>", 107))
    def test_identifiers_int(self):
        """test identifiers_int"""
        self.assertTrue(TestLexer.test('huy 2910_456', "huy,2910456,<EOF>", 108))
    def test_identifiers_7(self):
        """test identifiers_7"""
        self.assertTrue(TestLexer.test('b_123__456 ___huy1', "b_123__456,___huy1,<EOF>", 109))
    def test_identifiers_8(self):
        """test identifiers_8"""
        self.assertTrue(TestLexer.test('huylatro_2910___danghocppl danglam_testcase', "huylatro_2910___danghocppl,danglam_testcase,<EOF>", 110))
    def test_int_2(self):
        """test int_2"""
        self.assertTrue(TestLexer.test('1234_234_789 1_77822_21933 12_2910, 271_56_7_1234', "1234234789,17782221933,122910,,,2715671234,<EOF>", 111))
    def test_iden_int_2(self):
        """test iden_int_2"""
        self.assertTrue(TestLexer.test('0_12345', "0,_12345,<EOF>", 112))
    def test_iden_int_3(self):
        """test identifiers_8"""
        self.assertTrue(TestLexer.test('hello 123_456__2711', "hello,123456,__2711,<EOF>", 113))
    def test_iden_int_4(self):
        """test iden_int_4"""
        self.assertTrue(TestLexer.test('daddy2404_214 __mommy123 123__400', "daddy2404_214,__mommy123,123,__400,<EOF>", 114))
    def test_iden_int_5(self):
        """test iden_int_5"""
        self.assertTrue(TestLexer.test('lam100testcase_123 100__testcase', "lam100testcase_123,100,__testcase,<EOF>", 115))
    def test_iden_int_6(self):
        """test iden_int_6"""
        self.assertTrue(TestLexer.test('345_2910_231__abc', "3452910231,__abc,<EOF>", 116))
    def test_iden_int_7(self):
        """test iden_int_7"""
        self.assertTrue(TestLexer.test('hello  huy2910_2711', "hello,huy2910_2711,<EOF>", 117))
    def test_iden_9(self):
        """test identifiers_8"""
        self.assertTrue(TestLexer.test('hello huy \\t', "hello,huy,Error Token \\", 118))
    def test_iden_int_8(self):
        """test iden_10"""
        self.assertTrue(TestLexer.test('123_2910__2999__7111_ huydanghoc',"1232910,__2999__7111_,huydanghoc,<EOF>", 119))
    def test_iden_int_9(self):
        """test iden_int_9"""
        self.assertTrue(TestLexer.test('2999_102 _2910 2499_123__quan 4563_2242_2123__huy _', "2999102,_2910,2499123,__quan,456322422123,__huy,_,<EOF>", 120))
    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.test('do int = a ; a = a+1 while (x<1);', "do,int,=,a,;,a,=,a,+,1,while,(,x,<,1,),;,<EOF>", 121))
    def test_keyword_2(self):
        """test iden_keyword_2"""
        self.assertTrue(TestLexer.test('for (int i =1, i<2,i++) i = i*2', "for,(,int,i,=,1,,,i,<,2,,,i,+,+,),i,=,i,*,2,<EOF>", 122))
    def test_keyword_3(self):
        """test iden_keyword_3"""
        self.assertTrue(TestLexer.test('auto i =2; boolean flag = true; if (flag != true) i=i+2', "auto,i,=,2,;,boolean,flag,=,true,;,if,(,flag,!=,true,),i,=,i,+,2,<EOF>", 123))
    def test_keyword_4(self):
        """test iden_keyword_4"""
        self.assertTrue(TestLexer.test('if (string = "hello") i +=2 else if (i || a) a = a+b', "if,(,string,=,hello,),i,+,=,2,else,if,(,i,||,a,),a,=,a,+,b,<EOF>", 124))
    def test_keyword_5(self):
        """test iden_keyword_5"""
        self.assertTrue(TestLexer.test('float a =123_432.e10_234 function(a,b)', "float,a,=,123432.e10,_234,function,(,a,,,b,),<EOF>", 125))
    def test_keyword_6(self):
        """test iden_keyword_6"""
        self.assertTrue(TestLexer.test('if (a && b) return a else integer x =x+1', "if,(,a,&&,b,),return,a,else,integer,x,=,x,+,1,<EOF>", 126))
    def test_keyword_7(self):
        """test iden_keyword_7"""
        self.assertTrue(TestLexer.test('void testcase(integer a_bc) a_bc =1_234_456_33', "void,testcase,(,integer,a_bc,),a_bc,=,123445633,<EOF>", 127))
    def test_keyword_8(self):
        """test iden_keyword_8"""
        self.assertTrue(TestLexer.test('out of string = "hello huy" float = 1_342_21_2_34.2e+10', "out,of,string,=,hello huy,float,=,134221234.2e+10,<EOF>", 128))
    def test_keyword_9(self):
        """test iden_keyword_9"""
        self.assertTrue(TestLexer.test('inherit a = 123_234..2e1++12', "inherit,a,=,123234.,.2e1,+,+,12,<EOF>", 129))
    def test_keyword_10(self):
        """test iden_keyword_10"""
        self.assertTrue(TestLexer.test('array[] = 5 array[1_23,23_45] =8', "array,[,],=,5,array,[,123,,,2345,],=,8,<EOF>", 130))
    def test_float_1(self):
        """test float_1"""
        self.assertTrue(TestLexer.test('float a = 123._', "float,a,=,123.,_,<EOF>", 131))
    def test_float_2(self):
        """test float_2"""
        self.assertTrue(TestLexer.test('12_34_789_1.e2++3', "12347891.e2,+,+,3,<EOF>", 132))
    def test_float_3(self):
        """test float_3"""
        self.assertTrue(TestLexer.test('1_23432.234_235', "123432.234,_235,<EOF>", 133))
    def test_float_4(self):
        """test float_4"""
        self.assertTrue(TestLexer.test('1_234_67.e12+3_345 345.123e2++3', "123467.e12,+,3345,345.123e2,+,+,3,<EOF>", 134))
    def test_float_5(self):
        """test float_5"""
        self.assertTrue(TestLexer.test('.573e123+3e23_29', ".573e123,+,3e23,_29,<EOF>", 135))
    def test_float_6(self):
        """test float_6"""
        self.assertTrue(TestLexer.test('1_.3453e2 321e+2++.2e3', "1,_,.3453e2,321e+2,+,+,.2e3,<EOF>", 136))
    def test_float_7(self):
        """test float_7"""
        self.assertTrue(TestLexer.test('..233e-2+123_23.e2-123', ".,.233e-2,+,12323.e2,-,123,<EOF>", 137))
    def test_float_8(self):
        """test float_8"""
        self.assertTrue(TestLexer.test('float a_bc = 1234.e-2_.234e+2', "float,a_bc,=,1234.e-2,_,.234e+2,<EOF>", 138))
    def test_float_9(self):
        """test float_9"""
        self.assertTrue(TestLexer.test('float a_2113 123.234e2_2345+1234_22e+2', "float,a_2113,123.234e2,_2345,+,123422e+2,<EOF>", 139))
    def test_float_10(self):
        """test float_10"""
        self.assertTrue(TestLexer.test('1232..e222..e+2_234+21_21.e+1', "1232.,.e222,.,.e+2,_234,+,2121.e+1,<EOF>", 140))
    def test_float_11(self):
        """test float_11"""
        self.assertTrue(TestLexer.test('12342_23.234e2 123_2910.23042 1231e2 .392e+23 ', "1234223.234e2,1232910.23042,1231e2,.392e+23,<EOF>", 141))
    def test_string_12(self):
        """test string_12""" 
        self.assertTrue(TestLexer.test('"\\" hello everyone \\\""','\\" hello everyone \\\",<EOF>', 142))
    def test_float_13(self):
        """test float_13"""
        self.assertTrue(TestLexer.test('""', ",<EOF>", 143))
    def test_float_14(self):
        """test float_14"""
        self.assertTrue(TestLexer.test('123_234__.234e3+232.2e-2+123_29.27 ', "123234,__,.234e3,+,232.2e-2,+,12329.27,<EOF>", 144))
    def test_float_15(self):
        """test float_15"""
        self.assertTrue(TestLexer.test('234.23e+3_234.234e3 ', "234.23e+3,_234,.234e3,<EOF>", 145))
    def test_float_16(self):
        """test float_16"""
        self.assertTrue(TestLexer.test('8420.12e-1_2343+234.243+.2e-2', "8420.12e-1,_2343,+,234.243,+,.2e-2,<EOF>", 146))
    def test_float_17(self):
        """test float_17"""
        self.assertTrue(TestLexer.test('123_1232.422_12.e23_12', "1231232.422,_12,.e23,_12,<EOF>", 147))
    def test_float_18(self):
        """test float_18"""
        self.assertTrue(TestLexer.test('2331.23e+2-321.21',"2331.23e+2,-,321.21,<EOF>", 148))
    def test_float_19(self):
        """test float_19"""
        self.assertTrue(TestLexer.test('1234.23e--232_23.45', "1234.23,e,-,-,23223.45,<EOF>", 149))
    def test_float_20(self):
        """test float_20"""
        self.assertTrue(TestLexer.test('4921.21e+34_1234.234e-1+321_32e++2', "4921.21e+34,_1234,.234e-1,+,32132,e,+,+,2,<EOF>", 100))
    def test_51(self):
        """test comment """
        self.assertTrue(TestLexer.test(
            '/*Hi this is comment 2*/ _b: integer = 2;', '_b,:,integer,=,2,;,<EOF>', 151))

    def test_52(self):
        """test comment """
        self.assertTrue(TestLexer.test('/*Hi this is // hi comment 3*/ _c: integer = 3;', '_c,:,integer,=,3,;,<EOF>', 152))

    def test_53(self):
        """test comment """
        self.assertTrue(TestLexer.test('/*Hi this is comment 4 /*sasda comment*/ hi */ _d: string = 1_23_4;', 'hi,*,/,_d,:,string,=,1234,;,<EOF>', 153))

    def test_54(self):
        """test comment """
        self.assertTrue(TestLexer.test('/*Hi this /*sasda comment la comment 5*/ _e: string = 16_23_4;', '_e,:,string,=,16234,;,<EOF>', 154))

    def test_55(self):
        """test comment """
        self.assertTrue(TestLexer.test('_f: integer = 16_230_4; /*Hi this // la comment 6*/', '_f,:,integer,=,162304,;,<EOF>', 155))

    def test_56(self):
        """test comment """
        self.assertTrue(TestLexer.test('_g: string = 17.e-90; // hi single /* sasda */ comment', '_g,:,string,=,17.e-90,;,<EOF>', 156))

    def test_57(self):
        """test comment """
        self.assertTrue(TestLexer.test('// comment only no /* sasda */ other _cde 123_67', '<EOF>', 157))

    def test_58(self):
        """test comment """
        self.assertTrue(TestLexer.test('hi // comment only no // other _cde 123_67 /* hi sasda comment */', 'hi,<EOF>', 158))

    def test_59(self):
        """test comment """
        self.assertTrue(TestLexer.test('/* hi sasda comment // hi /*hi*/ hi */', 'hi,*,/,<EOF>', 159))

    def test_60(self):
        """test string """
        self.assertTrue(TestLexer.test('"Hi huy 12_34_5 _ab"', 'Hi huy 12_34_5 _ab,<EOF>', 160))

    def test_61(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\b djsdlksa djaslkdjsak"', 'String \\b djsdlksa djaslkdjsak,<EOF>', 161))

    def test_62(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\f djsdlksa djaslkdjsak"', 'String \\f djsdlksa djaslkdjsak,<EOF>', 162))

    def test_63(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\r djsdlksa djaslkdjsak"', 'String \\r djsdlksa djaslkdjsak,<EOF>', 163))

    def test_64(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\n djsdlksa djaslkdjsak"', 'String \\n djsdlksa djaslkdjsak,<EOF>', 164))

    def test_65(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\t djsdlksa djaslkdjsak"', 'String \\t djsdlksa djaslkdjsak,<EOF>', 165))

    def test_66(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\\' djsdlksa djaslkdjsak"', 'String \\\' djsdlksa djaslkdjsak,<EOF>', 166))

    def test_67(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\\\ djsdlksa djaslkdjsak"', 'String \\\\ djsdlksa djaslkdjsak,<EOF>', 167))

    def test_68(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\\\ \\\' \\t \\n \\r \\f jaskdjsad djsakldlsa dsajlkdsal"', 'String \\\\ \\\' \\t \\n \\r \\f jaskdjsad djsakldlsa dsajlkdsal,<EOF>', 168))

    def test_69(self):
        """test string """
        self.assertTrue(TestLexer.test('"djlksajdlksa dsakljdsa dakjsdaslkjd 123_4 _cde', 'Unclosed String: djlksajdlksa dsakljdsa dakjsdaslkjd 123_4 _cde', 169))

    def test_70(self):
        """test string """
        self.assertTrue(TestLexer.test('_ab = 123_67.e10 "String \\t dkjsdlksa qwqws 123_4 _cde', '_ab,=,12367.e10,Unclosed String: String \\t dkjsdlksa qwqws 123_4 _cde', 170))

    def test_71(self):
        """test string """
        self.assertTrue(TestLexer.test('1_0_23 integer "String without \\n unclose 123_4 _cde', '1023,integer,Unclosed String: String without \\n unclose 123_4 _cde', 171))

    def test_72(self):
        """test string """
        self.assertTrue(TestLexer.test('"String without \\n unclose \\t \\b', 'Unclosed String: String without \\n unclose \\t \\b', 172))

    def test_73(self):
        """test string """
        self.assertTrue(TestLexer.test('"a _cde 12_3', 'Unclosed String: a _cde 12_3', 173))

    def test_74(self):
        """test string """
        self.assertTrue(TestLexer.test('"String illegal escape \\a"', 'Illegal Escape In String: String illegal escape \\a', 174))

    def test_75(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\t \\n illegal escape \\d"', 'Illegal Escape In String: String \\t \\n illegal escape \\d', 175))

    def test_error_string_8(self):
        """test string """
        self.assertTrue(TestLexer.test('"String \\t \\n illegal \\g escape"', 'Illegal Escape In String: String \\t \\n illegal \\g', 176))
        
    def test_error_string_9(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\t \\n illegal \\h escape"', 'Illegal Escape In String: \\t \\n illegal \\h', 177))

    def test_78(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\t \\n \\f illegal \\q" escape', 'Illegal Escape In String: \\t \\n \\f illegal \\q', 178))

    def test_79(self):
        """test string """
        self.assertTrue(TestLexer.test('"Hi \\" world \\""', 'Hi \\" world \\",<EOF>', 179))

    def test_80(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\" \\""', '\\" \\",<EOF>', 180))

    def test_81(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\" hi everyone \\\""', '\\" hi everyone \\",<EOF>', 181))

    def test_82(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\" \\"\\" \\""', '\\" \\"\\" \\",<EOF>', 182))

    def test_83(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\" huy \\n \\"\\" \\""', '\\" huy \\n \\"\\" \\",<EOF>', 183))

    def test_84(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\" huy \\n \\"\\" \\" \\t \\f"', '\\" huy \\n \\"\\" \\" \\t \\f,<EOF>', 184))

    def test_85(self):
        """test string """
        self.assertTrue(TestLexer.test('""', ',<EOF>', 185))

    def test_86(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\"huy yeu Lam"', '\\"huy yeu Lam,<EOF>', 186))

    def test_87(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\"\\t"', '\\"\\t,<EOF>', 187))

    def test_88(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\"\\t Lam yeu \\" /*huy*/"', '\\"\\t Lam yeu \\" /*huy*/,<EOF>', 188))

    def test_89(self):
        """test string """
        self.assertTrue(TestLexer.test('"\\"\\t"', '\\"\\t,<EOF>', 189))

    def test_90(self):
        self.assertTrue(TestLexer.test('1_23 0_9', '123,0,_9,<EOF>', 190))

    def test_91(self):
        self.assertTrue(TestLexer.test('6_23.e1', '623.e1,<EOF>', 191))

    def test_92(self):
        self.assertTrue(TestLexer.test('true ab_123', 'true,ab_123,<EOF>', 192))

    def test_93(self):
        self.assertTrue(TestLexer.test('_123 = 9_01', '_123,=,901,<EOF>', 193))

    def test_94(self):
        self.assertTrue(TestLexer.test('-90_123 huy /*hi*/', '-,90123,huy,<EOF>', 194))

    def test_95(self):
        self.assertTrue(TestLexer.test('/*hi "world"*/', '<EOF>', 195))

    def test_96(self):
        self.assertTrue(TestLexer.test('/*hi "world"*/ 12_6E0156', '126E0156,<EOF>', 196))

    def test_97(self):
        self.assertTrue(TestLexer.test('.10e+2//', '.10e+2,<EOF>', 197))

    def test_98(self):
        self.assertTrue(TestLexer.test('2_1.1E-22//', '21.1E-22,<EOF>', 198))

    def test_99(self):
        self.assertTrue(TestLexer.test('2_1.1E-22//comment', '21.1E-22,<EOF>', 199))
    def test_100(self):
        self.assertTrue(TestLexer.test('2_11233', '211233,<EOF>', 99))
    
    

    


    
    
    
    