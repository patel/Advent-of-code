class Solution(object):
	def generateCharacterLookup(self, input):
		char_lookup = {'corrupted': [], 'incomplete': []}
		for l in input.splitlines():
			s = []
			is_corrupted = False
			for c in l:
				top = s[-1] if s else ''
				if c in ['(', '[', '{', '<']:
					s.append(c)
				elif ((c == ')' and top in list('[{<')) or (c == ']' and top in list('({<')) or (c =='}' and top in list('([<'))  or (c == '>' and top in list('([{'))):
					char_lookup['corrupted'].append(c)
					is_corrupted = True
					break
				elif ((c == ')' and top == '(') or (c == ']' and top == '[') or (c == '}' and top == '{') or (c == '>' and top == '<')):
					s.pop()
			if not is_corrupted:
				char_lookup['incomplete'].append(s)
		return char_lookup

	def calcScores(self, input):
		scoresLookup = {
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137
		}
		s = 0
		char_lookup = self.generateCharacterLookup(input)
		corrupted_chars = char_lookup['corrupted']
		for chars in corrupted_chars:
			s += scoresLookup.get(chars, 0)
		return s

	def calcMiddleScore(self, input):
		scoresLookup = {
		'(': 1,
		'[': 2,
		'{': 3,
		'<': 4
		}
		s = []
		char_lookup = self.generateCharacterLookup(input)
		incomplete_chars = char_lookup['incomplete']
		for l in incomplete_chars:
			l.reverse()
			s.append(reduce(lambda a,b: a*5+b, [scoresLookup.get(c, 0) for c in l], 0))
		s.sort()
		return s[len(s)/2]

input = """[[<[<{[<{{<[{(()[])[[]()]}[((){})<[]{}>]}<<{[]{}}<(){}>><([]<>)>>>[[[<<>>[<><>]][<<>>(<><>)]][{
((<[(<<(<{<((<()<>>{()()}){<<>><()[]>})([{<>{}}(()[])]{(<><>>})>(<((()())<[][]>)>([(<>{})({}())][<
<<<(<<[[((({<([]<>)[[]]>{<{}>{(){}}}}{[<[][]><<>[]>]({<><>}{()<>})})[<<({}())(()<>)>[([]{})<[]()>]>({[[]
<(<<<[((([{({((){})<<>{}>}[<(){}>[<>()]])[[<{}[]>({}{}]](<<>[]><[]<>>)]}](<[({[][]}<()<>>)<[
{<<<{[({{(<<(<<>[]><[]()>){<[][]>{<>{}}}>((({}())([]<>))[<{}{}>({}())])>(<<<()[]>><<<>{}>(()<
{<{<<[[(<<[{<<{}[]>>([<>()]{{}{}})}]<(<{<>()}{{}()}>{({}[])<<>()>})>>>){[{[{<[[]{}][<><>]>}{(<{}(
(((([(({((<[<(<>{})[{}{}]>](<[()<>]{<><>}>)><<[<[]{}>((){})]<[()[]]>>{[{<>()}((){})]({()[]}(()[]))}>))}(
<<[(({({(<{{((<>[])[[]<>])([<>]{()()})}<<{<>[]}><<{}()>>>}>)(<(<{<()[]><(){}>}{{(){}}[{}<>]}>{
(([[{<[<<{[<{<()[]>{<>[]}}{<{}{}>{[]<>}}>[{<{}{}>(<>[])}]]{<<({}[])>(<[]<>>[{}])>({{<>()}(<
(<{{(<<{[([<<{()[]}>{({}<>){<>[]}]>((<[]{}><{}{}>))]([{(()<>)(<>[])}]<<((){})<<>{}>>[(()[])
{{[[<<{<{{{([{()[]}[{}()]]{(<>{}){<><>}}){<[[][]][()[]]>}}<{{<[][]>[{}[]]>(<<>{}><{}{}>)}>}}<<{[{([](
{[<({{{[<{<{[([][])]{({}())<[][]>}}((<(){}>{()<>})<<<>{}>>)>}(((<{<>{}}<{}()>>)[((()()))[<<>{}>(
{{{[{{[(([{{[[{}<>]([]<>)]([(){}][[]()])}[{{[]<>}[{}()]}(<<><>>]]}][[([[[]<>]<<>{}>][{[]{}
<<{{{[{{[<({<<[]<>><{}<>>>}[[{()<>}{[]<>}]({(){}}{{}()})])[[(<<>[]>[[]])[{{}{}}[[]()]]]<((
({{[{{{{<[[({[{}{}]{[]<>}}<<()<>>(()<>)>)<{{(){}]<()()>}{{(){}}[<><>]}>]<<({{}{}}<(){}>)([{}
{([[[<<([[{{[<()<>>(()<>))({<>[]}(<>{}))}{(<{}()>{()[]})}}([[{{}[]}<[]>]<([]<>){<>}>])]<{[[([]{})]{(<><>)[[]<
([<<([<[[({((({}[]){[]{}}){({}[])({}<>)})>)[(<{{{}{}}[(){}]}(([][])<{}<>>)><[[<><>]{<>{}}]{{{}[]}{[][]}}>)<[[
{[<<{[<{[<{[[({}[])({}<>)]<<{}{}>{{}()}}]{[[<>{}]<[]{}>]}}(([(<><>){[][]}]([<>()]<()[]>))<[<()<>>(<><>)
(<[<[(({{<{<<[{}()]>(([]())<<>[]>)>}[{<[[]{}]([]<>)><{<><>}[()<>]>}{{{(){}}{[]{}}}}]>}}){{<{([<([]())({}())
<<{({{<[<[{([{{}<>}{<><>}]([(){}](()[]))){[{()[]}<<>()>]({()()}({}()))}}]<[<<(())(()[])>>{(<{}<>>{
{{{(<<[(<[([[[()<>]<()[]>]]{[[[]{}]{<>{}}]((<><>)({}{}))})]([(<{<>()}{[]{}}><<{}{}><<>[]>>)[<<()[]>((){
[{(<<{[<<([{[<[][]>][{()()}({}())]}]([{([]{})<{}<>>}(<()>[{}])]{<([]<>)<{}{}>>(({}<>)<<><>>)}))>([[((<<>{}
[[(<({{(({{(<[{}<>]([]{})>{[<>[]]([][])})[(<[]<>><{}()>)[<{}()>(())]]}<[<[[]{}]<{}{}>>{<()()>({}<>)}]<
([(<({(<{{(((<[]<>>{<>()})<{[]{}>([]{})>)[<[()<>]({}[])>[(<>{})(<>[])]]){<((<>{}){()[]})><{<[]<>><<><>>
({{<({(<<({[[{<><>}]<<<><>>({}[])>]([<[]<>>[{}()]]{{<>{}}({}[])}}}<{({[]<>}({}{}))[(<>())(<>())]}((([]{}){[][
(((({[(<([<[(<<>>[[][]])<{<><>}[{}<>]>]{({<>()}(<><>))(({}<>))}>])<([[<<()<>>{[][]}>]<[[[][
[<<(([({((<<{({}())}[(()()){[]<>}]>>){({<[{}{}]<<>()>>{<{}()>}})})})])[[<((<[{([<>()][{}[]])((()[])
{{{<{[[(<[{{<<{}()>[{}<>]>{({}{})<()>}}(<[(){}]>(<(){}>[[]]))}(<<[[]{}}({})><[<>[]]{<><>}>><[<[]<>>{<><>}](((
{<[[<[{{<((<[<<>()><[]{}>][<{}()><{}{}>]>)[[[[[][]]<()[]}][([]{})(()())]]])>[[((<{[]<>}<()>><[{}[]](<><>)>
<{([{[{[{([({<{}[]>([]<>)}[[[][]]<()()>])[<[{}()]>{<<><>>(()<>)}]]){({(<[]<>>([]<>))[(<>){
[{{<(({<{[{<{({})(<>[])}({<><>}{[]()})>(({[]<>}(<>{}))[{()()}{{}<>}])}{<{{<>()}<[]{})}(<()><(
{(<[{[[{{<(([{{}{}}<()[]>]<[<><>]>)([(<><>)])){<<{[]{}}[[][]]>{[[]<>]{<>{}}}>[<<[][]><<>()>><<{}<>>[<>()>>]}>
<[{{(<<{{{[[{<[]<>>(()<>)}<{()<>}{<>[]}>]<[<()()>]{<<>>([]())}>]{([<<>{}>({}<>)])[({{}}{[]<>})[
<<[[<<[(<{{{[{()[]}([]())][[[]]((){})]}}(([{[][]}[()()]]<<()>[{}[]]>))}>)<{({{<[[][]]{()()}><<{}{}
{[<(([([{({([({}()){<><>}][((){})([]())])[<<()<>>(<>())>{[[]()}(()[])}]}<{{<(){}>{()[]}}((<><>){{}<>})}((
{(({([[{{((([<()()>([][])]<<{}[]>[<>]>)(<{<><>}[{}{}]>[[<>{}]]))[{<<[][]>[()]><[{}{}]>}{<([]<>)([]<>)>}]
(({[[<<<{[{([(<>[])<()[]>])(<([])({}{})>)}[{(<<>{}>({}<>))}<<[<>[]>[(){}]>(<{}{}>)>]]{([[<<>()>
[{[[{([({[{(({()[]}[[]<>])<[[]<>]([])>)([{{}{}}[{}[]]]<{{}<>}>)][<(<<>[]>{<><>})<(()<>){[][]}>>[[{[]{}}([]())
([[{({([({<<(<[]<>>)[{()[]}<<>()>]><<{<>()}<<>[]>>[[<>{}]<<><>>]>)<<<<<>[]><<><>>>[[[]]]>[{
[{{([(<[[<{((([]{})[()()])[<[]{}>[<>()]])<[{()()}(<>{})]({[]}[<>{}])>}((<{[]()}>)({<{}{}>[
[[[{{[[[<<(<(({}())[<>{}])<{{}<>}(()())>>[[((){})][[[]{}]{()}]])>>{[(<([{}{}]({}<>))([{}()]<<>[]])>({<
{<{({(({{{[{<(<>{})>{<{}<>>(<><>)}}<(<[]()>[[][]])<[{}()]>>]<{{<()[]>{{}()}}{<{}[]>{{}{}}}}{{<()<>><<>
[{[<{[<<({(<{{<>()}({}<>)}<(<>[])[()()]>>{{{<>()}{()[]}}})<{<({}()){<>{}}>({<>[]}({}())]}>}(
[[{<([((({([{{()[]}<[]{}>}({<>[]}[<><>])]{{<[]<>>[<><>]}[{()()}[<>[]]]})}[{[<{()()}(<>))<({}){()<>}>]([
(<(<{[{<({[{{{[]()}({}{})}{<{}[]><<>{}>}}]})>}<{[[(<[<[]{}>([]())](<{}>[()()])>)][(([{[]<>
<<<<{<{<<[<({<[]>({}<>)})<[{[][]}[[]()]][[{}<>]<{}[]>])>([(([][])[[]()])<[{}[]]{[]{}}>](<[{}()]{{}()}
({[[([([<{[[({()[]}[<>[]])[<[][]><<>{}>>][(({}{})(<>[])){(<>[])}]]<{{{{}()}[<>[]]}<[[]<>]([]())>}>}{<{({
((<{<{{[((<<<(()<>)<[]{}>>[<[][]>[(){}]]>>)){([[[[<>]({}<>)]{{{}<>}([]{})}]<[<<>()>(()())][{[]{}}{[]<>}]>]
{<<{{[({[<{{(<{}[]><<>[]>)([[]()])}<[{{}{}}{<><>}]<({})<{}()>>>}<[([{}<>][<>{}])](<<{}[]><<
{[{[[<<[(({[(((){}){<>[]})]([[<>[]]][<<>{}>[<><>]])})({<[({}[])<{}[]>]>}<(<(()<>)[[]{}]][[()()][<><
((<<[({<{[[({<[]()>([]())}[<[]{}>(()<>)])]<<{[{}[]][<>()]}><<{<>[]}[()<>]>[<[]{}>{[]()}]>>][(({[<>
{{<[{<([({{([<<><>>{{}()}][<[][]>{[]()}])[<[[]]{[]<>}>]}(({<()[]>[{}()]}<[[]<>]{<>()}>))})])<{[{<[<[{}{}]
[(({({[[<{(<{{<>[]}[()<>]}((<>{})<<>[]>)>{[<(){}>{{}<>}]])[<{(<>[]){{}[]}}([()()][<>[]])>((({}())
{(([<{([[{([<<{}()><[][]>>[(<>()){()[]}]]<[<()()>[{}]]([{}<>][{}[]])>){<{[[]<>]<<>{}>}{([]{})}>[([
<{[{({([(<<{<[()<>]<(){}>>(<()>{[][]})})>{[([<{}{}>[<>()]])[{([]()){<>{}}}<<{}<>>>]]})])([<(([{<(){}>[{
<<<(([<[{[[<{({}()>{[]()}}>]]([<[[()][{}[]]]<[()()]{(){}}>><<({}[])(()<>)>{(()[])}>]{[(<[]()>)[{[]{}}
(({(([[<{(<{[(<>[]]]}<(({}{}))([[][]]([][]))>><[{(()())[()<>]}<{(){}}>]>)((<{{()[]}{<>()}}<([
[[[{<[{<[<[[{(<>{})<[]()>}{(()[])[<>()]}][<({}()>[<><>]>{<[]{}><[][]>}]]><<{[{(){}}{{}{}}][<<><
((([<<((<[{(([<>[]]([]{}))([<>]{<>()})}([[(){}][[]()]][(<><>){{}()}])}{[<[()<>]({}<>)>[<{}{}>]][<(<>())<[]
{<<{([(((([{<[()]{(){}}>{{{}[]}}}[{(()[]){()<>}}{<<>>[<>{}]}]]<[{(<>())(()[])}]>){[[<({}{})[()[]]>{[{}(
([{(({([([(<<{<>[]}<{}<>>>[[[]{}]<[]{}>]>((([]<>)<<>[]>)[[(){}]]))[<{{<>{}}}[(<>}{()()}]><{<<>{}><
{(<[<{({([{{([[][]]>({()()}[[][]])}[<(()())([]())><(<><>)([]{})>]}[(({{}{}}{{}<>})([<><>]<()[]>))]
((<(<<{{{{<{{(()<>)({}{})}{{<>[]}<()[]>}}<<<[][]>(()[])>[[()[]][[]()]]>>[[{{[]{}}[[][]]}][<[()[]]{[]<>}>
(((<(<<<{{<{<{{}{}}(()<>)>[((){})[()[]]]}{[[<>[]]{{}()}][{()[]}({}{})]}>}}>{[{<<{[{}()]}<[[]()]
({(([[<{[{<(([[]()](<><>))[<{}[]){{}()}])(<[()[]]<[]()>>[<{}<>>[()<>]])>[<[[()()]<<>[]>][([]())([]{})]>{{<<>(
[[(([((([<[[<{{}<>}({}[])>[([]<>)[()[]]]]<[(()())({}<>)](([]<>)<[]()>)>]>[{{{(()<>)}<{[]()}
(<(({[<<{((<[[[]()]{{}<>}]<<{}()>({}[])>>)<{{({}){()()}}<{[][]}>}>){[(<<[]<>>[{}{}]>{{(){}}{[
{<(<(<<{<(<{{[{}[]]([]{})}([{}[]](<>))}[([<>()]{[]{}})<({}<>){<><>}>]>[{<[[][]]>}[<[<><>](()())>(([
{(<(<{<(<<{{{<(){}>}({[][]}{{}{}})}}<(<<<>()>[(){}]>(<{}()>{{}}))>>[{{[{[]{}}(()[])]}[((<>())<<
([((([[{([{<<((){})>{{<>}{[]()}}>{[((){})<()[]>]<{[]{}}[(){}]>}}{((<{}()><{}>)){{<{}[]>[[]
{{{(<<{((([[{(<>{})({}())}[<[]()>({}{})]]<<[{}]>{[[]()]{()[]}}>]{({<()[]>((){})})<{<[]<>>{{}{}
(<<[[([{{(<<({{}}[{}{}])<([]{}){<>()}>>>(({<()()>({}[])}<<{}()>[(){}]>)))[{([{<>[]}([]())]([()()][<>{}])){
<(<(<<<([[[(<{{}[]}{{}[]}>[[<>()]{()[]}])]<{({{}()}{{}<>})<({}[])([]<>)>}{(({}[])(<>{}))((()<>)<[]()>)}>](<
<<{(([<([[[[<{<>()}({}[])>{((){})[{}()]}]}[<{<<>[]><[]<>>}<[{}<>]{{}()}>>{{(()())[()[]]}{<()<>
(({<<[{([{<(([{}[]][(){}])[<[]()>(()<>)]}>}<[(<{{}()}{{}<>}><[[]()][[]()]>)]<(<(<>())>({<>[]})){[{(){}}<{}{}>
({[[{[{{<(([[[{}{}]<(){}>]((()[])(()[]))]({([]<>)({}{})}{<<>{}>{<>}}))<{(<[]{}>(()()))[[()[]](<><>)
([{[{{<{{(<[((<>){[]()})(({}())[<><>])]>({[(<><>}{{}[]}]{(()[])[()]}}{([[]{}](<><>))<<{}[]>(<>())>}))
<[(([[[<{[[(({()[]}<<>[]>){{<><>}<(){}>})<([()]{<>[]}){{<>{}}}>]]<[{{([]())({}{}>}<{[][]}<<>{}>
({(<{<([[<{[<{[]()}[{}<>>>[[(){}][[]{}]]][{[()<>][<><>]}{<()()>}]}<({{(){}}<()()>}{[<><>](<>())})[(
([({<[<[{({<<[<>{})[<><>]>{{[]{}}}>[[{()<>}([]{})](({}<>)<<>>)]}<{<<<>>{()[]}>}<{<[]()>}>>)(<<<{
({<{[[({[([{[{[]{}}{[]<>}](((){})({}()))}]([<{<>{}}{()<>}>{({}{})(()())}])}]<{({{<()[]>{()}}
({[[{[((<[[[{<<>[]>(<>[])}]]{<({{}[]}){[{}{}]<<>()>}>[([<>()]{{}()})(<()()><<>[]>)]}]>(<([{<[]{}>(()())}<{[
[<<<{<({({{<{[<><>]{{}<>}}{<(){}>}>}})})[<<[{[{({}{})<<>>}[{[]}(()())]]{{([]())([]())}{({}[])[<>
<<<[[((<{{<(((<>[])(()))<<<>()><<>{}>>)<[{<>[]}{(){}}]{[{}]({}())}>>}}[[((({()}{[][]}){<{}[]>}
(<[<({[[{[<<[(<>[])]([[]<>]<[]{}>)>({(<>[])([]())}<[{}<>)<<>{}>>)>[{<[[][]]><[{}<>]<[]()>>}<<[
{[({<<<<(<([{{[][]}}]{<{<>()}<<>()>>[({}())<[]{}>]})>)>>><<<{{((([{}[]]<<><>>)[[[][]]({}[])])<{<{}{}>(
[[[({((({<([({[][]}{[]})<({}[]}[{}{}]>][([[]()]([]()))<<()<>>>])<[<<()[]><()[]>>]>>([<<{[]()}{[][]}><
[{{<<<({<({(<<<><>>>{(<>[])[<><>]})<(<<>{}>(()()))[{{}()}{(){}}]}}[(<{[]()}<[]<>>>({<>{}}[{}
([<<{<[{([<[<{<>{}}<[]{}>><([][]>>][{([][])[()()]}<<[]<>>>]>][{<({<>()}<[][]>)[[[]<>]{()<>}
({<<[<(<<<(<((()<>)<{}<>>)>)<<([<>{}][<>[]])<<()()>({}[])>>([(()())(()<>)]{{{}<>}<[]{}>})>>>>[
<{[{<[[<[(<{({<><>}{[]<>}){<[]{}><()>}}({({})[[]{}]})>{(<{[]<>}{<><>}>([{}[]]{<><>}))(<<{}()>[
<{{<[[({{{<({<[]()>[{}[]]}<{<><>}{()<>}>)[<<[]{}>{{}<>}>[<<>[]>((){})]]>}}(<[[(([][])[{}<>]){(()<>)[()[]]}]((
[{[{<[(({{({<{{}{}}<()()>>(<[]<>>{<>[]})}(<<()[]>{()<>}>))<<<[{}{}]<<>[]>>>[[{[]{}}]((()<>){<>
{[[<{({[<(<((<{}[]>){[{}[]]})[{[{}{}]({}())}]>(<{{()<>}(<><>)}[(<><>)<[]{}]]><{<()[]>([][])"""
s = Solution()
print(s.calcScores(input))
print(s.calcMiddleScore(input))

