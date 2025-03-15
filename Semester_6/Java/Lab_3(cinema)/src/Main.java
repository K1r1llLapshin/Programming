public class Main {
    public static void main(String[] args) throws Exception {
       TicketSystem ticketSystem = new TicketSystem();
       ticketSystem.setCinema("First");
       ticketSystem.setCinemaHall("First", 2, 3);
       ticketSystem.setSesion("First", 0, "Session1", 23, 200);

       ticketSystem.setCinema("Second");
       ticketSystem.setCinemaHall("Second", 2, 3);
       ticketSystem.setCinemaHall("Second", 4, 6);
       ticketSystem.setSesion("Second", 0, "Session2", 23, 200);
       ticketSystem.setSesion("Second", 1, "Session3", 23, 200);
       ticketSystem.setSesion("Second", 1, "Session4", 23, 200);
       System.out.print("");
    }

    
}
