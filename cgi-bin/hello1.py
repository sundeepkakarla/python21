#!/usr/bin/env python
print "Content-type: text/html"
print 
print """
<html>
<h1>hello world</h1>
<form action="action1.py" method="post">
	<input type="text" name="info"/>
	<input type="submit" value="submit"/>
</form>
</html>

"""

