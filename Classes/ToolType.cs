public class ToolType
{
    private string _Name;
    private string _Category;
    private int _Quantity;
    private int _OnHand;
    private int _CheckedOut;
    private int _TimesCheckedOut;
    private int _Cost;
    private List<Tool> _ToolList = new List<Tool>();

    public string Name {
        get { return _Name; }
        set { _Name = value; }
    }

    public string Category {
        get { return _PhoneNumber; }
        set { _PhoneNumber = value; }
    }

    public int Quantity {
        get { return _Quantity; }
        set { _Quantity = value; }
    }

    public int OnHand {
        get { return _OnHand; }
        set { _OnHand = value; }
    }

    public int CheckedOut {
        get { return _CheckedOut; }
        set { _CheckedOut = value; }
    }

    public string _TimesCheckedOut {
        get { return _TimesCheckedOut; }
        set { _TimesCheckedOut = value; }
    }

    public double Cost {
        get { return _Cost; }
        set { _Cost = value; }
    }

    public List<Tool> ToolList {
        get { return _OnHand; }
        set { _OnHand = value; }
    }
    
    public void addTool() {

    }
}