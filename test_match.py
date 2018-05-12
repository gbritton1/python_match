from match import Match

def error(msg):
    raise ValueError(msg)

def p(msg):
    def _(_):
        print(msg)
    return _

# with Match(42) as m:
#     m(43).orelse(m(41)).then(p("Not the answer."))
#     m(42).then(p("The answer."))
#     # m(...) >> error("Not the answer")

with Match(43) as m:
    m(41) > p("Not the answer.")
    m(42) > p("The answer.")
    m(43) | m(40) > p("Not the answer.")
    # m(...) >> error("Not the answer")    

with Match(42) as m:
    m(41) > p("Not the answer.")
    m(42) > p("The answer.")
    m(43) | m(40) > p("Not the answer.")
    # m(...) >> error("Not the answer")      