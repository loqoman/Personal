/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Point;

/**
 * Encapsulates an oval shape. The shape is defined by a bounding rectangle;
 * the origin is the upper-left hand corner of the rectangle.
 * <p>
 * <img src="{@docRoot}/doc-files/oval.png" alt = "(oval picture)">
 * </p>
 * 
 * @author jack
 */
public class Oval extends Rectangle
{

    /**
     * Default constructor. The origin, fill color and edge color are set
     * to null; the width and height of the bounding rectangle will be 0.
     */
    public Oval()
    {
        this( null, null, null, 0, 0 );
    }
        
    /**
     * Sets the origin, width and height of the oval to the given values.
     * The fill and edge colors are set to null.
     * 
     * @param origin    The given origin.
     * @param width     The given width
     * @param height    The given height.
     */
    public Oval( DPoint origin, double width, double height )
    {
        this( origin, null, null, width, height );
    }

    /**
     * Defines an oval shape based on the given parameters.
     * 
     * @param origin    The given origin.
     * @param fillColor The given fill color.
     * @param edgeColor The given edge color.
     * @param width     The given width.
     * @param height    The given height.
     */
    public Oval(
        DPoint origin,
        Color fillColor,
        Color edgeColor, 
        double width, 
        double height 
    )
    {
        super( origin, fillColor, edgeColor, width, height );
    }
    
    /**
     * Draws this oval.
     * 
     * @param gtx The graphics context to control the drawing.
     */
    public void draw( Graphics2D gtx )
    {
        Color   save    = gtx.getColor();
        Color   fill    = getFillColor();
        Color   edge    = getEdgeColor();
        Point   orig    = getOrigin().getPoint();
        int     width   = getIntWidth();
        int     height  = getIntHeight();
        
        if ( fill != null )
        {
            gtx.setColor( fill );
            gtx.fillOval( orig.x, orig.y, width, height );
        }
        
        if ( edge != null )
        {
            gtx.setColor( edge );
            gtx.drawOval( orig.x, orig.y, width, height );
        }
        
        gtx.setColor( save );
    }
}
