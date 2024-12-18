import java.sql.*;
public class FetchRecord
{
	public static void main(String args[])
	{
		Connection cn;
		Statement stmt;
		ResultSet rs;
		try
		{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			cn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:OraHome","system","mjkacc");
			if(cn!=null)
			{
				System.out.println("Connection sucessfull");
				stmt=cn.createStatement();
				stmt.execute("create table kv(id number(30),name varchar(30))");
				System.out.println("table created");
				stmt.execute("insert into kv values(1,'kriyanshi')");
				stmt.execute("insert into kv values(2,'rutvi')");


				rs=stmt.executeQuery("select * from kriyanshi1");
				while(rs.next())
				{
					System.out.println(rs.getInt(1)+" "+rs.getString(2)+" ");
				}
			}
			else 
			{
				System.out.println("not connected...");
			}
		}
			catch(Exception e)
			{
				e.printStackTrace();
			}
		
	}
}