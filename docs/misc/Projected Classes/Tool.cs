public class Tool
{
    private string _Id;
    private string _DateCheckedOut;

    public string Id {
        get { return _Id; }
        set { _Id = value; }
    }

    public string DateCheckedOut {
        get { return _DateCheckedOut; }
        set { _DateCheckedOut = value; }
    }
    
    public void Checkout() {

    }
}