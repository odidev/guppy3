# Tests generated by: guppy.gsl.Tester
# Date: Thu May 14 11:30:45 2020
class Tester:
    tests = {}
    def test_example_kind(self, arg):
        t0 = arg.m_returns()
        t1 = t0.range(1)
        t2 = t0.range(1, 1)
        t3 = t0.range(1, 1, 1)
        t4 = t0.a_nokind
        t5 = t0.m_alt([])
        t6 = t0.m_repeat('abc', 'abc')
        t7 = t0.m_repeat(1, 'abc', 'abc')
        t8 = t0.m_repeat('abc', 'abc', 'abc')
        t9 = t0.m_repeat(1, 'abc', 'abc', 'abc')
        t10 = t0.m_repeat('abc', 'abc', 'abc', 'abc')
        t11 = t0.m_repeat(1, 'abc', 'abc', 'abc', 'abc')
        t12 = t0.m_draw_keywords()
        t13 = t0.m_draw_keywords(a=1)
        t14 = t0.m_draw_keywords(b=1)
        t15 = t0.m_noargs()
        t16 = t0.m_draw_keywords(a=1, b=1)
        t17 = t0.m_draw_keywords(c='abc')
        t18 = t0.m_draw_keywords(a=1, c='abc')
        t19 = t0.m_draw_keywords(b=1, c='abc')
        t20 = t0.m_draw_keywords(a=1, b=1, c='abc')
        t21 = t0.m_one(1)
        t22 = t0.m_opt()
        t23 = t0.m_opt(1)
        t24 = t0.m_opt(1, 'abc')
        t25 = t0.m_alt(1)
        t26 = t0.m_alt('abc')
        t27 = arg.range(1)
        t28 = arg.range(1, 1)
        t29 = arg.range(1, 1, 1)
        t30 = arg.a_nokind
        t31 = arg.m_alt([])
        t32 = arg.m_repeat('abc', 'abc')
        t33 = arg.m_repeat(1, 'abc', 'abc')
        t34 = arg.m_repeat('abc', 'abc', 'abc')
        t35 = arg.m_repeat(1, 'abc', 'abc', 'abc')
        t36 = arg.m_repeat('abc', 'abc', 'abc', 'abc')
        t37 = arg.m_repeat(1, 'abc', 'abc', 'abc', 'abc')
        t38 = arg.m_draw_keywords()
        t39 = arg.m_draw_keywords(a=1)
        t40 = arg.m_draw_keywords(b=1)
        t41 = arg.m_noargs()
        t42 = arg.m_draw_keywords(a=1, b=1)
        t43 = arg.m_draw_keywords(c='abc')
        t44 = arg.m_draw_keywords(a=1, c='abc')
        t45 = arg.m_draw_keywords(b=1, c='abc')
        t46 = arg.m_draw_keywords(a=1, b=1, c='abc')
        t47 = arg.m_one(1)
        t48 = arg.m_opt()
        t49 = arg.m_opt(1)
        t50 = arg.m_opt(1, 'abc')
        t51 = arg.m_alt(1)
        t52 = arg.m_alt('abc')
    tests['.tgt.docexample.example_kind'] = test_example_kind
