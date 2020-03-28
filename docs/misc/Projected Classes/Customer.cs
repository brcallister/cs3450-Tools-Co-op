public class Customer
{
    private string _Name;
    private string _PhoneNumber;
    private string _Address;
    private string _Email;
    private string _Password;

    public String Name {
        get { return _Name; }
        set { _Name = value; }
    }

    public String PhoneNumber {
        get { return _PhoneNumber; }
        set { _PhoneNumber = value; }
    }

    public String Address {
        get { return _Address; }
        set { _Address = value; }
    }

    public String Email {
        get { return _Email; }
        set { _Email = value; }
    }

    public String Password {
        get { return _Password; }
        set { _Password = value; }
    }
    
    public void payDues() {

    }

    public bool verifyPassword() {
        
    }
}