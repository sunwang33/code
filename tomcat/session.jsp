<%@ page language="java"%>
<html>
	<head>
		<title>Tomcat A</title>
	</head>
	<body>
		<h1><font> color="blue">web1.test.com</font></h1>
		<table align="centre" border="1">
			<tr>
					<td>Session ID</td>
		<% session.setAttribute("test.com","test.com");%>
					<td><%=session.getId() %></td>
			</tr>
			<tr>
				<td>Created on</td>
				<td><%=session.getCreationTime()%></td>
			</tr>
		</table>
	</body>
</html>