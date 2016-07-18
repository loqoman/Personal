package edu.pcwe.uw.javaintro.shapes;

/**
 * Stores a coordinate pair (x, y) as two double values.
 * @author jack
 */
public class DPoint
{
    private static final double EPSILON   = .0001;
    /** The x coordinate. */
    public double x = 0;
    /** The y coordinate. */
    public double y = 0;

    /**
     * Default constructor. Coordinates are set to (0, 0).
     */
    public DPoint()
    {
        this( 0, 0 );
    }

    /**
     * Initializes a coordinate pair;
     * @param xco   x coordinate value
     * @param yco   y coordinate value
     */
    public DPoint( double xco, double yco )
    {
        x = xco;
        y = yco;
    }

    /**
     * Copy constructor.
     * @param   point   The point to copy.
     */
    public DPoint( DPoint point )
    {
        this( point.x, point.y );
    }

    /**
     * Converts this coordinate pair to a <code>java.awt.Point</code>.
     * The coordinates are rounded to the nearest integer
     * prior to conversion.
     *
     * @return A <code>java.awt.point</code> instance rounded
     *         from this coordinate pair.
     */
    public java.awt.Point getPoint()
    {
        int xco = (int)(x + .5);
        int yco = (int)(y + .5);

        java.awt.Point  point   = new java.awt.Point( xco, yco );
        return point;
    }

    /**
     * Calculate the distance from this point to another point.
     * @param other The other point to which to calculate the distance.
     * @return The distance from this point to <em>other.</em>
     */
    public double getDistanceTo( DPoint other )
    {
        double  xDiffSquared    = Math.pow( x - other.x, 2 );
        double  yDiffSquared    = Math.pow( y - other.y, 2 );
        double  dist            = Math.sqrt( xDiffSquared + yDiffSquared );
        return dist;
    }

    /**
     * Gets a description of this coordinate pair.
     * @return A description of this coordinate pair.
     */
    @Override
    public String toString()
    {
        String  descrip =
            "(" + x + "," + y + ")";

        return descrip;
    }
    
    /**
     * Calculates a hash code for this object.
     * @return  Hash code for this object.
     */
    @Override
    public int hashCode()
    {
        int hash    = Double.hashCode( x ) ^ Double.hashCode( y );
        return hash;
    }
    
    /**\
     * Determine if this object is equal to another. The other object
     * is equal to this if it is non-null; type DPoint; and the x and 
     * y values are the same.
     * @param obj The other object to test for equality.
     * @return  True if this object is equal to <em>obj.</em>
     */
    @Override
    public boolean equals( Object obj )
    {
        boolean rcode   = false;
        
        if ( this == obj )
            rcode = true;
        else if ( obj != null && obj instanceof DPoint )
        {
            DPoint  that    = (DPoint)obj;
            if ( areEqual( x, that.x ) && areEqual( y, that.y ) )
                rcode = true;
        }
        
        return rcode;
    }
    
    private static boolean areEqual( double num1, double num2 )
    {
        double  diff    = Math.abs( num1 - num2 );
        boolean rcode   = diff < EPSILON;
        return rcode;
    }
}
