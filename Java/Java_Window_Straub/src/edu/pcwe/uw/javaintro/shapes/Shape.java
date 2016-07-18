package edu.pcwe.uw.javaintro.shapes;

import java.awt.Color;
import java.awt.Graphics2D;

/**
 * Abstract base class for implementing a shape.
 * 
 * @author jack
 */
public abstract class Shape
{
    private DPoint                      origin;
    private Color                       fillColor;
    private Color                       edgeColor;
    
    /**
     * Draws the given shape on a canvas. Drawing resources available
     * in the base class are <em>origin, fillColor</em> and <em>edgeColor.</em>
     * This method must be implemented
     * according to the following rules:
     * <ol>
     * <li>
     * Any resource may be null.
     * </li>
     * <li>
     * If the origin is null, it must be treated as equivalent to 
     * DPoint( 0, 0 ).
     * </li>
     * <li>
     * If fillColor is null, the interior of the shape must not be drawn.
     * </li>
     * <li>
     * If edgeColor is null, the edge of the shape must not be drawn.
     * </li>
     * </ol>
     * Any 
     * 
     * @param graphics  The graphics context that controls the 
     *                  drawing area.
     */
    public abstract void draw( Graphics2D graphics );
    
    /**
     * Default constructor. This method is equivalent to calling
     * Shape( null, null, null ).
     * 
     * @see #Shape( DPoint, Color, Color)
     */
    public Shape()
    {
        this( null, null, null );
    }
    
    /**
     * Constructor. The origin is set to the given value, and 
     * the fill and edge colors are set to null.
     * 
     * @param origin The given value for the origin.
     * 
     * @see #Shape( DPoint, Color, Color)
     */
    public Shape( DPoint origin )
    {
        this( origin, null, null );
    }
    
    /**
     * Constructor. Sets a Shape's origin, fill color and edge color
     * to the given values. Any argument may be null.
     * 
     * @param origin    The given origin.
     * @param fillColor The given fill color.
     * @param edgeColor The given edge color.
     */
    public Shape( DPoint origin, Color fillColor, Color edgeColor )
    {
        this.origin = origin;
        this.fillColor = fillColor;
        this.edgeColor = edgeColor;
    }

    /**
     * Gets the origin of the containing Shape.
     * 
     * @return The origin of the containing Shape.
     * 
     * @see #setOrigin( DPoint ) 
     */
    public DPoint getOrigin()
    {
        return origin;
    }

    /**clears
     * Sets the origin of the containing Shape.
     * 
     * @param origin The origin to set.
     * 
     * @see #getOrigin() 
     */
    public void setOrigin(DPoint origin)
    {
        this.origin = origin;
    }

    /**
     * Gets the fill color of the containing Shape.
     * 
     * @return The fill color of the containing Shape.
     * 
     * @see #setFillColor(java.awt.Color) 
     */
    public Color getFillColor()
    {
        return fillColor;
    }

    /**
     * Sets the fill color of the containing Shape.
     * 
     * @param fillColor The fill color for the containing Shape.
     * 
     * @see #setFillColor(java.awt.Color) 
     */
    public void setFillColor(Color fillColor)
    {
        this.fillColor = fillColor;
    }

    /**
     * Gets the edge color of the containing Shape.
     * 
     * @return The edge color of the containing Shape.
     * 
     * @see #setEdgeColor(java.awt.Color) 
     */
    public Color getEdgeColor()
    {
        return edgeColor;
    }

    /**
     * Sets the fill color of the containing Shape.
     * 
     * @param edgeColor The edge color for the containing Shape.
     * 
     * @see #setFillColor(java.awt.Color) 
     */
    public void setEdgeColor(Color edgeColor)
    {
        this.edgeColor = edgeColor;
    }
}
