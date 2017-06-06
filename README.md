# aries-analyzer
A tiny package to analyze a class's GPA's using a pdf generated from Aries Gradebook.

Roadmap:
The minimum viable product is a script that finds the pdf output by Aries,
then extracts the text from it, then calculates each student's GPA and displays those
as well as the class average, an an easily copy/pastable format.
This should be able to be run on Mac and Windows without any extra installation/packages.

The plan is to use the package "slate" to extract the text, some regular
expressions to parse it, and TkInter to have a nice portable GUI. Then, wrap it
all up into a native executable with no dependencies using py2exe and py2app.
