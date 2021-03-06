case_while = '''
var n = 5;
var p = 1;
while(n > 0)
{
  p = p * n;
  n = n - 1;
}
log(p, n);
'''

case_function = '''
var inc = function(a) {
  return a + 1;
};
log(inc(1));
'''

case_if = '''
if (true)
{
  log(1);
}
else
{
  log(2);
}
'''

case_recursion = '''
var fac = function(n) {
  if (n <= 1)
  {
    return 1;
  }
  return n * fac(n - 1);
};
log(fac(6));
'''

case_Y = '''
var Y = function (F) {
  return (function (x) {
            return F(function (y) { return (x(x))(y);});
         })
         (function (x) {
            return F(function (y) { return (x(x))(y);});
         });
};

var FactGen = function (fact) {
  return (function(n) {
            if (n == 0) {
              return 1;
            } else {
              return n * fact(n - 1);
            }
         });
};

log((Y(FactGen))(7));
'''