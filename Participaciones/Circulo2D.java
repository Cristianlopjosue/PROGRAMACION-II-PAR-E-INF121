public class Circulo2D {
    private double x;
    private double y;
    private double r;

    public Circulo2D(double x, double y, double r) {
        this.x = x;
        this.y = y;
        this.r = r;
    }

    public Circulo2D() {
        this(0.0, 0.0, 1.0);
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getR() {
        return r;
    }

    public double getArea() {
        return Math.PI * Math.pow(r, 2);
    }

    public double getPerimetro() {
        return 2 * Math.PI * r;
    }

    public boolean contiene(double Px, double Py) {
        double D = Math.sqrt(Math.pow(Px - x, 2) + Math.pow(Py - y, 2));
        return D <= r;
    }

    public boolean circuloDentro(Circulo2D c) {
        double D = Math.sqrt(Math.pow(c.x - this.x, 2) + Math.pow(c.y - this.y, 2));
        return D + c.r <= this.r;
    }

    public boolean sobrepone(Circulo2D c) {
        double D = Math.sqrt(Math.pow(c.x - this.x, 2) + Math.pow(c.y - this.y, 2));
        return (Math.abs(this.r - c.r) <= D && D <= (this.r + c.r));
    }

public static void main(String[] args) {
        Circulo2D c1 = new Circulo2D(2, 0, 1);
        System.out.println("Área = " + c1.getArea());
        System.out.println("Perímetro = " + c1.getPerimetro());
        System.out.println("¿Contiene el punto? = " + c1.contiene(2.5, 0));
        System.out.println("¿Contiene el círculo? = " + c1.circuloDentro(new Circulo2D(2, 0, 0.5)));
        System.out.println("¿Se sobreponen? = " + c1.sobrepone(new Circulo2D(0, 0, 2)));
    }
}


