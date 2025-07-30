package model;

public class User {

	private int id;
	private String name;
	private String email;
	private String passwd;
	
	
	public User(String name, String email, String passwd) {
		this.name = name;
		this.email = email;
		this.passwd = passwd;
	}
	

	public int getId() {
		return id;
	}

	public String getName() {
		return name;
	}

	public String getEmail() {
		return email;
	}

	public String getPasswd() {
		return passwd;
	}


	@Override
	public String toString() {
		return "Id:"+id+", 이름:"+name+", 이메일:"+email;
	}	
}





