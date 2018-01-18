export default {
    AddRule : `We will prove that:
\\[\\int f(x) + g(x) \\, dx = \\int f(x) dx + \\int g(x) dx\\]

Using the fundamental theorem of calculus:
\\[\\frac{d}{dx} \\left( \\int f(x) + g(x) \\, dx \\right) = f(x) + g(x)\\]
\\[\\frac{d}{dx} \\left( \\int f(x) \\, dx + \\int g(x) \\, dx \\right) = f(x) + g(x)\\]
\\[\\therefore \\int f(x) + g(x) \\, dx = \\int f(x) dx + \\int g(x) \\, dx\\]`,

    ConstantRule : `We will prove that:
    \\[\\int a \\, dx = ax\\]
    
    We know that:
    \\[\\frac{d}{dx} ax = a\\]
    So, the antiderivative of \\(a\\) is \\(ax\\).`,

    ConstantTimesRule : `We will prove that:
    \\[\\int af(x) \\, dx = a \\int f(x) \\, dx\\]
    
    \\[\\frac{d}{dx}\\left( \\int af(x) \\, dx \\right) = a f(x)\\]
    \\[\\frac{d}{dx}\\left( a\\int f(x) \\, dx \\right) = a f(x)\\]
    \\[\\therefore \\int af(x) \\, dx = a \\int f(x) \\, dx\\]
    `,

    PowerRule : `We will prove that:
    \\[\\int x^a \\, dx = \\frac{x^{a+1}}{a+1}\\]
    
    We derive \\(\\frac{x^{a+1}}{a+1}\\) using the quotient rule:
    \\[\\frac{d}{dx} \\left( \\frac{x^{a+1}}{a+1} \\right) = \\frac{(a+1)(a+1)x^a}{(a+1)^2} = x^a\\]
    So, the antiderivative of \\(x^a\\) is \\(\\frac{x^{a+1}}{a+1}\\).
    `
}