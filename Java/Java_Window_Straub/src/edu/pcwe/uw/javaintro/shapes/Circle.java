/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import java.awt.Color;

/**
 * This class is a specialization of Oval, where the width and height
 * of the oval are equal. The circle is defined by its center and radius.
 * @author jack
 */
public class Circle extends Oval
{
    /**
     * Default constructor. The center of the circle is set to (0, 0),
     * the fill and edge colors are set to null and the radius is set to 0.
     */
    public Circle()
    {
        this( new DPoint( 0, 0 ), null, null, 0 );
    }
        
    /**
     * Defines a circle according to the given center and radius. The fill
     * and edge colors are set to njll.
     * 
     * @param center    The given center.
     * @param radius    The given radius.
     */
    public Circle( DPoint center, double radius )
    {
        this( center, null, null, radius );
    }

    /**
     * Defines a circle according to the given parameters.
     * 
     * @param center    The given center.
     * @param fillColor The given fill color.
     * @param edgeColor The given edge color.
     * @param radius    The given radius.
     */
    public Circle(
        DPoint center,
        Color fillColor,
        Color edgeColor, 
        double radius
    )
    {
        super( null,
               fillColor,
               edgeColor,
               radius * 2,
               radius * 2
        );
        
        DPoint  origin  = new DPoint( -radius, -radius );
        if ( center == null )
            origin  = new DPoint( -radius, -radius );
        else
            origin  = new DPoint( center.x - radius, center.y - radius );
        setOrigin( origin );
    }
    
    /**
     * Returns the radius of the circle.
     * 
     * @return The radius of the circle.
     */
    public double getRadius()
    {
        double  radius  = getWidth() * .5;
        return radius;
    }
    
    /**
     * Returns the center of the circle.
     * 
     * @return The center of the circle.
     */
    public DPoint getCenter()
    {
        double  radius  = getRadius();
        DPoint  origin  = getOrigin();
        double  xco     = origin.x + radius;
        double  yco     = origin.y + radius;
        DPoint  center  = new DPoint( xco, yco );
        
        return center;
    }
}
