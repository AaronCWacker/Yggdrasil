import streamlit as st
import graphviz as graphviz
import pandas as pd
import numpy as np

st.title('Graphviz Gallery: https://graphviz.org/gallery/')

# Plan
graph = graphviz.Digraph()
graph.edge('Plan', 'Intervention')
graph.edge('Intervention', 'Care')
graph.edge('Intervention', 'Category')
graph.edge('Intervention', 'QualityMeasure')
graph.edge('Intervention', 'Target')
graph.edge('Plan', 'Goal')
graph.edge('Plan', 'OutcomeScores')
graph.edge('Plan', 'Problem')
graph.edge('Problem', 'Domain')
graph.edge('Problem', 'Outcome')
graph.edge('Problem', 'Scope')
graph.edge('Problem', 'SignSymptom')
graph.edge('Problem', 'Urgency')
graph.edge('Plan', 'Pathway')
graph.edge('Pathway', 'Intervention')
graph.edge('Pathway', 'ProblemGoal')
graph.edge('Plan', 'SignSymptom')
graph.edge('Plan', 'Stage')
graph.edge('Plan', 'Delegate')
graph.edge('Plan', 'Note')
graph.edge('Plan', 'Person')
graph.edge('Problem', 'Association')
graph.edge('Problem', 'History')
graph.edge('Goal', 'History')
graph.edge('Intervention', 'Work')
graph.edge('Intervention', 'History')
graph.edge('SignSymptom', 'History')
graph.edge('Plan', 'Publication')
graph.edge('Publication', 'History')
graph.edge('Publication', 'Status')
st.graphviz_chart(graph)


# Assessment
graph = graphviz.Digraph()
graph.edge('Assessment', 'Score')
graph.edge('Assessment', 'QuestionAsked')
graph.edge('Assessment', 'ProgressChange')
graph.edge('Assessment', 'Programs')
graph.edge('Assessment', 'Product')
graph.edge('Assessment', 'Program')
graph.edge('Program', 'Population')
graph.edge('Assessment', 'Plan')
graph.edge('Plan', 'Question')
graph.edge('Plan', 'Problem')
graph.edge('Assessment', 'Response')
graph.edge('Response', 'Choice')
graph.edge('Response', 'Populator')
graph.edge('Assessment', 'Section')
graph.edge('Section', 'Score')
graph.edge('Assessment', 'Template')
graph.edge('Template', 'Script')
graph.edge('Template', 'Question')
graph.edge('Question', 'SubQuestion')
graph.edge('Question', 'Table')
graph.edge('Table', 'SubTable')
graph.edge('Table', 'Column')
graph.edge('Column', 'Choice')
graph.edge('Question', 'Response')
graph.edge('Response', 'ResponseTable')
graph.edge('Response', 'ResponseText')
graph.edge('Template', 'Section')
graph.edge('Assessment', 'Document')
graph.edge('Assessment', 'Service')
graph.edge('Service', 'History')
graph.edge('Service', 'Request')
st.graphviz_chart(graph)


# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('Grandpa', 'Ancestors')
graph.edge('Grandma', 'Ancestors')
graph.edge('Uncle', 'Grandma')
graph.edge('Aunt', 'Grandma')
graph.edge('Mom', 'Grandma')
graph.edge('Cousin Bob', 'Aunt')
graph.edge('Cousin Sue', 'Aunt')
graph.edge('Brother', 'Mom')
graph.edge('Sister', 'Mom')
st.graphviz_chart(graph)


st.graphviz_chart(''' 
digraph G2 {
    node [shape=plaintext];
    struct1 [label=<<TABLE>
      <TR><TD><IMG SRC="1.png"></IMG></TD></TR>
      <TR><TD>caption</TD></TR>
    </TABLE>>];
}
''')



st.title('Graphviz Dot Language: https://graphviz.org/doc/info/lang.html')

# Using graph language:
st.graphviz_chart(''' 
digraph G {
  rankdir=LR
  node [shape=plaintext]
  a [
     label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR><TD ROWSPAN="3" BGCOLOR="yellow">class</TD></TR>
  <TR><TD PORT="here" BGCOLOR="lightblue">qualifier</TD></TR>
</TABLE>>
  ]
  b [shape=ellipse style=filled
     label=<
<TABLE BGCOLOR="bisque">
  <TR>
      <TD COLSPAN="3">elephant</TD> 
      <TD ROWSPAN="2" BGCOLOR="chartreuse" 
          VALIGN="bottom" ALIGN="right">two</TD>
  </TR>
  <TR>
    <TD COLSPAN="2" ROWSPAN="2">
      <TABLE BGCOLOR="grey">
        <TR><TD>corn</TD></TR> 
        <TR><TD BGCOLOR="yellow">c</TD></TR> 
        <TR><TD>f</TD></TR> 
      </TABLE>
    </TD>
    <TD BGCOLOR="white">penguin</TD> 
  </TR> 
  <TR>
    <TD COLSPAN="2" BORDER="4" ALIGN="right" PORT="there">4</TD>
  </TR>
</TABLE>>
  ]
  c [ 
  label=<long line 1<BR/>line 2<BR ALIGN="LEFT"/>line 3<BR ALIGN="RIGHT"/>>
  ]
  subgraph { rank=same b c }
  a:here -> b:there [dir=both arrowtail=diamond]
  c -> b
  d [shape=triangle]
  d -> c [label=<
<TABLE>
  <TR>
    <TD BGCOLOR="red" WIDTH="10"> </TD>
    <TD>Edge labels<BR/>also</TD>
    <TD BGCOLOR="blue" WIDTH="10"> </TD>
  </TR>
</TABLE>>
  ]
}
''')

st.graphviz_chart(''' 
digraph R {
  rankdir=LR
  node [style=rounded]
  node1 [shape=box]
  node2 [fillcolor=yellow, style="rounded,filled", shape=diamond]
  node3 [shape=record, label="{ a | b | c }"]
  node1 -> node2 -> node3
}
''')

st.title('Vega Lite Example: https://docs.streamlit.io/library/api-reference/charts/st.vega_lite_chart ')
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
     'mark': {'type': 'circle', 'tooltip': True},
     'encoding': {
         'x': {'field': 'a', 'type': 'quantitative'},
         'y': {'field': 'b', 'type': 'quantitative'},
         'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},
     },
 })

# More graph examples

st.graphviz_chart(''' 
digraph structs {
    node [shape=record];
    struct1 [label="<f0> left|<f1> mid&#92; dle|<f2> right"];
    struct2 [label="<f0> one|<f1> two"];
    struct3 [label="hello&#92;nworld |{ b |{c|<here> d|e}| f}| g | h"];
    struct1:f1 -> struct2:f0;
    struct1:f2 -> struct3:here;
}
''')

st.graphviz_chart(''' 
graph G {
  fontname="Helvetica,Arial,sans-serif"
  node [fontname="Helvetica,Arial,sans-serif"]
  edge [fontname="Helvetica,Arial,sans-serif"]
  layout=fdp
  e
  subgraph clusterA {
    a -- b;
    subgraph clusterC {
      C -- D;
    }
  }
  subgraph clusterB {
    d -- f
  }
  d -- D
  e -- clusterB
  clusterC -- clusterB
}
''')

st.graphviz_chart(''' 
graph Transparency {
	layout=neato
	start=11 // empiric value to set orientation
	bgcolor="#0000ff11"
	node [shape=circle width=2.22 label="" style=filled]
	5 [color="#0000ff80"]
	6 [color="#ee00ee80"]
	1 [color="#ff000080"]
	2 [color="#eeee0080"]
	3 [color="#00ff0080"]
	4 [color="#00eeee80"]
	1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 1
	}
''')

st.graphviz_chart('''
digraph UML_Class_diagram {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	labelloc="t"
	label="UML Class diagram demo"
	graph [splines=false]
	node [shape=record style=filled fillcolor=gray95]
	edge [arrowhead=vee style=dashed]
	Client -> Interface1 [xlabel=dependency]
	Client -> Interface2
	edge [dir=back arrowtail=empty style=""]
	Interface1 -> Class1 [xlabel=inheritance]
	Interface2 -> Class1 [dir=none]
	Interface2 [label="" xlabel="Simple\ninterface" shape=circle]
	Interface1[label = <{<b>«interface» I/O</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	Class1[label = <{<b>I/O class</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	edge [dir=back arrowtail=empty style=dashed]
	Class1 -> System_1 [xlabel=implementation]
	System_1 [label = <{<b>System</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	"Shared resource" [label = <{<b>Shared resource</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	edge [dir=back arrowtail=diamond]
	"System_1" -> Subsystem_1 [xlabel="composition"]
	Subsystem_1[label = <{<b>Subsystem 1</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	Subsystem_2[label = <{<b>Subsystem 2</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	Subsystem_3[label = <{<b>Subsystem 3</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	"System_1" -> Subsystem_2
	"System_1" -> Subsystem_3
	edge [xdir=back arrowtail=odiamond]
	Subsystem_1 -> "Shared resource" [xlabel=aggregation]
	{Subsystem_2 Subsystem_3 } -> "Shared resource"
}
''')



st.graphviz_chart('''
digraph G {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	subgraph cluster_1 {
		node [ style=filled,shape="box",fillcolor="antiquewhite:aquamarine" ]n5;
		node [ shape="ellipse",fillcolor="bisque4:blue2" ]n4;
		node [ shape="circle",fillcolor="cadetblue1:chocolate1" ]n3;
		node [ shape="diamond",fillcolor="crimson:cyan4" ]n2;
		node [ shape="triangle",fillcolor="deepskyblue2:firebrick" ]n1;
		node [ shape="pentagon",fillcolor="gray24:gray88" ]n0;
		label = "X11 Colors";
	}
	subgraph cluster_2 {
		node [ style=filled,shape="box",fillcolor="bisque:brown" ]n11;
		node [ shape="ellipse",fillcolor="green:darkorchid" ]n10;
		node [ shape="circle",fillcolor="deepskyblue:gold" ]n9;
		node [ shape="diamond",fillcolor="lightseagreen:orangered" ]n8;
		node [ shape="triangle",fillcolor="turquoise:salmon" ]n7;
		node [ shape="pentagon",fillcolor="snow:black" ]n6;
		label = "SVG Colors";
	}
	subgraph cluster_3 {
		node [ style=filled,shape="box",fillcolor="/accent3/1:/accent3/3" ]n17;
		node [ shape="ellipse",fillcolor="/accent4/1:/accent4/4" ]n16;
		node [ shape="circle",fillcolor="/accent5/1:/accent5/5" ]n15;
		node [ shape="diamond",fillcolor="/accent6/1:/accent6/6" ]n14;
		node [ shape="triangle",fillcolor="/accent7/1:/accent7/7" ]n13;
		node [ shape="pentagon",fillcolor="/accent8/1:/accent8/8" ]n12;
		label = "Brewer - accent";
	}
	subgraph cluster_4 {
		node [ style=filled,shape="box",fillcolor="/blues3/1:/blues3/2" ]n23;
		node [ shape="ellipse",fillcolor="/blues4/1:/blues4/3" ]n22;
		node [ shape="circle",fillcolor="/blues5/1:/blues5/4" ]n21;
		node [ shape="diamond",fillcolor="/blues6/1:/blues6/5" ]n20;
		node [ shape="triangle",fillcolor="/blues7/1:/blues7/6" ]n19;
		node [ shape="pentagon",fillcolor="/blues8/1:/blues8/7" ]n18;
		label = "Brewer - blues";
	}
n3 -> n9 -> n15 -> n21;
}
''')

st.graphviz_chart('''
digraph G {bgcolor="#0000FF44:#FF000044" gradientangle=90
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
		fillcolor="darkgray:gold";
		gradientangle=0
		node [fillcolor="yellow:green" style=filled gradientangle=270] a0;
		node [fillcolor="lightgreen:red"] a1;
		node [fillcolor="lightskyblue:darkcyan"] a2;
		node [fillcolor="cyan:lightslateblue"] a3;
		a0 -> a1 -> a2 -> a3;
		label = "process #1";
	}
	subgraph cluster_1 {
		node [fillcolor="yellow:magenta" 
			 style=filled gradientangle=270] b0;
		node [fillcolor="violet:darkcyan"] b1;
		node [fillcolor="peachpuff:red"] b2;
		node [fillcolor="mediumpurple:purple"] b3;
		b0 -> b1 -> b2 -> b3;
		label = "process #2";
		color=blue
		fillcolor="darkgray:gold";
		gradientangle=0
		style=filled;
	}
	start -> a0;
	start -> b0;
	a1 -> b3;
	b2 -> a3;
	a3 -> a0;
	a3 -> end;
	b3 -> end;
	start [shape=Mdiamond ,
		fillcolor="pink:red",
		gradientangle=90,
		style=radial];
	end [shape=Msquare,
		fillcolor="lightyellow:orange",
		style=radial,
		gradientangle=90];
}
''')

st.graphviz_chart('''
graph Color_wheel {
	graph [
		layout = neato
		label = "Color wheel, 33 colors.\nNeato layout"
		labelloc = b
		fontname = "Helvetica,Arial,sans-serif"
		start = regular
		normalize = 0
	]
	node [
		shape = circle
		style = filled
		color = "#00000088"
		fontname = "Helvetica,Arial,sans-serif"
	]
	edge [
		len = 2.7
		color = "#00000088"
		fontname = "Helvetica,Arial,sans-serif"
	]
	subgraph Dark {
		node [fontcolor = white width = 1.4]
		center [width = 1 style = invis shape = point]
		center -- darkred [label = "0°/360°"]
		darkred [fillcolor = darkred]
		brown [fillcolor = brown]
		brown -- center [label = "30°"]
		olive [fillcolor = olive]
		olive -- center [label = "60°"]
		darkolivegreen [fillcolor = darkolivegreen fontsize = 10]
		darkolivegreen -- center [label = "90°"]
		darkgreen [fillcolor = darkgreen]
		darkgreen -- center [label = "120°"]
		"dark hue 0.416" [color = ".416 1 .6" fontcolor = white]
		"dark hue 0.416" -- center [label = "150°"]
		darkcyan [fillcolor = darkcyan]
		darkcyan -- center [label = "180°"]
		"dark hue 0.583" [color = ".583 1 .6" fontcolor = white]
		"dark hue 0.583" -- center [label = "210°"]
		darkblue [fillcolor = darkblue]
		darkblue -- center [label = "240°"]
		"dark hue 0.750" [color = ".750 1 .6"]
		"dark hue 0.750" -- center [label = "270°"]
		darkmagenta [fillcolor = darkmagenta]
		darkmagenta -- center [label = "300°"]
		"dark hue 0.916" [color = ".916 1 .6"]
		"dark hue 0.916" -- center [label = "330°"]
	}
	subgraph Tue {
		node [width = 1.3]
		"hue 0.083" -- brown
		"hue 0.083" [color = ".083 1 1"]
		"hue 0.125" [color = ".125 1 1"]
		"hue 0.166" -- olive
		"hue 0.166" [color = ".166 1 1"]
		"hue 0.208" [color = ".208 1 1"]
		"hue 0.250" -- darkolivegreen
		"hue 0.250" [color = ".250 1 1"]
		"hue 0.291" [color = ".291 1 1"]
		"hue 0.333" -- darkgreen
		"hue 0.333" [color = ".333 1 1"]
		"hue 0.375" [color = ".375 1 1"]
		"hue 0.416" -- "dark hue 0.416"
		"hue 0.416" [color = ".416 1 1"]
		"hue 0.458" [color = ".458 1 1"]
		"hue 0.500" -- darkcyan
		"hue 0.500" [color = ".500 1 1"]
		"hue 0.541" [color = ".541 1 1"]
		node [fontcolor = white]
		"hue 0.000" [color = ".000 1 1"]
		"hue 0.000" -- darkred
		"hue 0.041" [color = ".041 1 1"]
		"hue 0.583" -- "dark hue 0.583"
		"hue 0.583" [color = ".583 1 1"]
		"hue 0.625" [color = ".625 1 1"]
		"hue 0.666" -- darkblue
		"hue 0.666" [color = ".666 1 1"]
		"hue 0.708" [color = ".708 1 1"]
		"hue 0.750" -- "dark hue 0.750"
		"hue 0.750" [color = ".750 1 1"]
		"hue 0.791" [color = ".791 1 1"]
		"hue 0.833" -- darkmagenta
		"hue 0.833" [color = ".833 1 1"]
		"hue 0.875" [color = ".875 1 1"]
		"hue 0.916" -- "dark hue 0.916"
		"hue 0.916" [color = ".916 1 1"]
		"hue 0.958" [color = ".958 1 1"]
		edge [len = 1]
		"hue 0.000" -- "hue 0.041" -- "hue 0.083" -- "hue 0.125" -- "hue 0.166" -- "hue 0.208"
		"hue 0.208" -- "hue 0.250" -- "hue 0.291" -- "hue 0.333" -- "hue 0.375" -- "hue 0.416"
		"hue 0.416" -- "hue 0.458" -- "hue 0.500" --"hue 0.541" -- "hue 0.583" -- "hue 0.625"
		"hue 0.625" -- "hue 0.666" -- "hue 0.708" -- "hue 0.750" -- "hue 0.791" -- "hue 0.833"
		"hue 0.833" -- "hue 0.875" -- "hue 0.916" -- "hue 0.958" -- "hue 0.000"
	}
	subgraph Main_colors {
		node [width = 2 fontsize = 20]
		red [fillcolor = red fontcolor = white]
		orangered [fillcolor = orangered]
		orange [fillcolor = orange]
		gold [fillcolor = gold]
		yellow [fillcolor = yellow]
		yellowgreen [fillcolor = yellowgreen]
		deeppink [fillcolor = deeppink fontcolor = white]
		fuchsia [label = "fuchsia\nmagenta" fillcolor = fuchsia fontcolor = white]
		purple [fillcolor = purple fontcolor = white]
		blue [fillcolor = blue fontcolor = white]
		cornflowerblue [fillcolor = cornflowerblue]
		deepskyblue [fillcolor = deepskyblue]
		aqua [fillcolor = aqua label = "aqua\ncyan"]
		springgreen [fillcolor = springgreen]
		green [fillcolor = green]
		purple -- fuchsia -- deeppink -- red
		cornflowerblue -- blue -- purple
		cornflowerblue -- deepskyblue -- aqua [len = 1.7]
		aqua -- springgreen -- green -- yellowgreen -- yellow
		yellow -- gold -- orange -- orangered -- red [len = 1.6]
		orange -- "hue 0.083"
		deeppink -- "hue 0.916"
		deeppink -- "hue 0.875"
		red -- "hue 0.000"
		yellowgreen -- "hue 0.250"
		blue -- "hue 0.666"
		yellow -- "hue 0.166"
		gold -- "hue 0.125"
		green -- "hue 0.333"
		springgreen -- "hue 0.416"
		aqua -- "hue 0.500"
		cornflowerblue -- "hue 0.583"
		deepskyblue -- "hue 0.541"
		purple -- "hue 0.791"
		purple -- "hue 0.750"
		fuchsia -- "hue 0.833"
	}
	subgraph Light_colors {
		node [width = 2 fontsize = 20]
		node [shape = circle width = 1.8]
		edge [len = 2.1]
		pink [fillcolor = pink]
		pink -- red
		lightyellow [fillcolor = lightyellow]
		lightyellow -- yellow
		mediumpurple [fillcolor = mediumpurple]
		mediumpurple -- purple
		violet [fillcolor = violet]
		violet -- fuchsia
		hotpink [fillcolor = hotpink]
		hotpink -- deeppink
		"light hue 0.250" [color = ".250 .2 1"]
		"light hue 0.250" -- yellowgreen
		lightcyan [fillcolor = lightcyan]
		lightcyan -- aqua
		lightslateblue [fillcolor = lightslateblue]
		lightslateblue -- blue
		lightgreen [fillcolor = lightgreen]
		lightgreen -- green
		lightskyblue [fillcolor = lightskyblue]
		lightskyblue -- deepskyblue
		peachpuff [fillcolor = peachpuff]
		peachpuff -- orange
		"light hue 0.416" [color = ".416 .2 1"]
		"light hue 0.416" -- springgreen
	}
	subgraph Tints {
		node [width = 1]
		edge [len = 2.4]
		"hue 0 tint" -- pink
		"hue 0 tint" [color = "0 .1 1"]
		"hue 0.041 tint" [color = ".041 .1 1"]
		"hue 0.083 tint" -- peachpuff
		"hue 0.083 tint" [color = ".083 .1 1"]
		"hue 0.125 tint" [color = ".125 .1 1"]
		"hue 0.166 tint" -- lightyellow
		"hue 0.166 tint" [color = ".166 .1 1"]
		"hue 0.208 tint" [color = ".208 .1 1"]
		"hue 0.250 tint" -- "light hue 0.250"
		"hue 0.250 tint" [color = ".250 .1 1"]
		"hue 0.291 tint" [color = ".291 .1 1"]
		"hue 0.333 tint" -- lightgreen
		"hue 0.333 tint" [color = ".333 .1 1"]
		"hue 0.375 tint" [color = ".375 .1 1"]
		"hue 0.416 tint" -- "light hue 0.416"
		"hue 0.416 tint" [color = ".416 .1 1"]
		"hue 0.458 tint" [color = ".458 .1 1"]
		"hue 0.5 tint" -- lightcyan
		"hue 0.5 tint" [color = ".5 .1 1"]
		"hue 0.541 tint" -- lightskyblue
		"hue 0.541 tint" [color = ".541 .1 1"]
		"hue 0.583 tint" [color = ".583 .1 1"]
		"hue 0.625 tint" [color = ".625 .1 1"]
		"hue 0.666 tint" -- lightslateblue
		"hue 0.666 tint" [color = ".666 .1 1"]
		"hue 0.708 tint" [color = ".708 .1 1"]
		"hue 0.750 tint" -- mediumpurple
		"hue 0.750 tint" [color = ".750 .1 1"]
		"hue 0.791 tint" [color = ".791 .1 1"]
		"hue 0.833 tint" -- violet
		"hue 0.833 tint" [color = ".833 .1 1"]
		"hue 0.875 tint" [color = ".875 .1 1"]
		"hue 0.916 tint" -- hotpink
		"hue 0.916 tint" [color = ".916 .1 1"]
		"hue 0.958 tint" [color = ".958 .1 1"]
		edge [len = 2]
		"hue 0 tint" -- "hue 0.041 tint" -- "hue 0.083 tint" -- "hue 0.125 tint" -- "hue 0.166 tint" -- "hue 0.208 tint"
		"hue 0.208 tint" -- "hue 0.250 tint" -- "hue 0.291 tint" -- "hue 0.333 tint" -- "hue 0.375 tint" -- "hue 0.416 tint"
		"hue 0.416 tint" -- "hue 0.458 tint" -- "hue 0.5 tint" --"hue 0.541 tint" -- "hue 0.583 tint" -- "hue 0.625 tint"
		"hue 0.625 tint" -- "hue 0.666 tint" -- "hue 0.708 tint" -- "hue 0.750 tint" -- "hue 0.791 tint" -- "hue 0.833 tint"
		"hue 0.833 tint" -- "hue 0.875 tint" -- "hue 0.916 tint" -- "hue 0.958 tint" -- "hue 0 tint"
	}
	}
''')
