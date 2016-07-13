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
 * This class encapsulates a rectangular shape.
 * 
 * @see Shape
 * 
 * @author jack
 */
public class Rectangle extends Shape
{
    private double      width;
    private double      height;
    
    /**
     * Default constructor. Sets the origin, fill color and edge color to null;
     * sets the width and height to 0.
     */
    public Rectangle()
    {
        this( null, null, null, 0, 0 );
    }
    
    /**
     * Constructor. Initializes the origin, width and height from the given
     * parameters. Fill and edge colors are set to null.
     * 
     * @param origin    The given origin.
     * @param width     The given width.
     * @param height    The given height.
     */
    public Rectangle( DPoint origin, double width, double height )
    {
        this( origin, null, null, width, height );
    }
    
    /**
     * Constructor.
     * 
     * @param origin    The origin for the rectangle.
     * @param fillColor The rectangle's fill color.
     * @param edgeColor THe rectangle's edge color.
     * @param width     THe rectangle's width.
     * @param height    THe rectangle's  height.
     * 
     * @see Shape#Shape(edu.pcwe.uw.javaintro.shapes.DPoint, java.awt.Color, java.awt.Color) 
     */
    public Rectangle(
        DPoint origin,
        Color fillColor,
        Color edgeColor, 
        double width, 
        double height 
    )
    {
        super( origin, fillColor, edgeColor );
        this.width = width;
        this.height = height;
    }
    
    /**
     * Draws this rectangle.
     * @param graph The graphics context drawing the rectangle.
     */
    public void draw( Graphics2D graph )
    {
        Color       save        = graph.getColor();
        Color       fill        = getFillColor();
        Color       edge        = getEdgeColor();
        Point       origin      = getOrigin().getPoint();
        int         iWidth      = getIntWidth();
        int         iHeight     = getIntHeight();
        
        if ( fill != null )
        {
            graph.setColor( fill );
            graph.fillRect( origin.x, origin.y, iWidth, iHeight );
        }
        
        if ( edge != null )
        {
            graph.setColor( edge );
            graph.drawRect( origin.x, origin.y, iWidth, iHeight );
        }
        
        graph.setColor( save );
    }

    /**
     * Gets the width of the rectangle.
     * @return The width of the rectangle.
     */
    public double getWidth()
    {
        return width;
    }

    /**
     * Gets the width of the rectangle rounded to the nearest integer.
     * @return The width of the rectangle rounded to the nearest integer..
     */
    public int getIntWidth()
    {
        int iWidth  = (int)Math.round( width );
        return iWidth;
    }

    /**
     * Sets the width of the rectangle to the given value.
     * 
     * @param width The width of the rectangle.
     */
    public void setWidth(double width)
    {
        this.width = width;
    }

    /**
     * Gets the height of the rectangle.
     * @return The height of the rectangle.
     */
    public double getHeight()
    {
        return height;
    }

    /**
     * Gets the height of the rectangle rounded to the nearest integer.
     * @return The height of the rectangle rounded to the nearest integer..
     */
    public int getIntHeight()
    {
        int iHeight = (int)Math.round( height );
        return iHeight;
    }

    /**
     * Sets the height of the rectangle to the given value.
     * @param height The height of the rectangle.
     */
    public void setHeight(double height)
    {
        this.height = height;
    }
}
