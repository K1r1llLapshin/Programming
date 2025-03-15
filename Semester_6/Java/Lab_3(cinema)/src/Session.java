public class Session {

    private String name;
    private int session_start;
    private int duration;

    Session(String name, int session_start, int duration){
        this.name = name;
        this.session_start = session_start;
        this.duration = duration;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getName(){
        return name;
    }

    public void setSesionStart(int session_start){
        this.session_start = session_start;
    }

    public int getSesionStart(){
        return session_start;
    }

    public void setDuration(int duration){
        this.duration = duration;
    }

    public int getDuration(){
        return duration;
    }

    public boolean equalSession (Session session){
        if (this.name.equals(session.getName()) && this.session_start == session.getSesionStart() && this.duration == session.getDuration())
            return true;
        else
            return false;
    }
}
