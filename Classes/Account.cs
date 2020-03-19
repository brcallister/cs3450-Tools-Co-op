public class Customer
{
    private int _AccountNumber;
    private bool _isActive;
    private int _FeesDue;
    private List<Tool> _CheckedOutTools = new List<Tool>();

    public int AccountNumber {
        get { return _AccountNumber; }
        set { _AccountNumber = value; }
    }

    public bool isActive {
        get { return _isActive; }
        set { _PhoneNumber = value; }
    }

    public int FeesDue {
        get { return _FeesDue; }
        set { _FeesDue = value; }
    }

    public List<Tool> CheckedOutTools {
        get { return _CheckedOutTools; }
        set { _CheckedOutTools = value; }
    }
    
    public void activateAccount() {

    }
}