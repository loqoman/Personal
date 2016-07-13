/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import edu.pcwe.uw.javaintro.shapes.util.ThreadUtils;
import java.awt.Color;
import javax.swing.JOptionPane;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author jack
 */
public class CircleTest
{
    public CircleTest()
    {
    }

    @Test
    public void testDefaultConstructor()
    {
        Circle  circle      = new Circle();
        DPoint  expCenter   = new DPoint( 0, 0 );
        
        assertEquals( expCenter, circle.getCenter() );
        assertEquals( 0, circle.getRadius(), .001 );
        assertNull( circle.getEdgeColor() );
        assertNull( circle.getFillColor() );
    }
    
    @Test
    public void testDPointDoubleConstructor()
    {
        DPoint  center  = new DPoint( .1, .2 );
        double  radius  = 4.5;
        Circle  circle  = new Circle( center, radius );
        
        assertEquals( center, circle.getCenter() );
        assertEquals( radius, circle.getRadius(), .001 );
        assertNull( circle.getEdgeColor() );
        assertNull( circle.getFillColor() );
    }
    
    @Test
    public void testDPointColorColorDoubleConstructor()
    {
        Color   edge    = Color.RED;
        Color   fill    = Color.BLUE;
        DPoint  center  = new DPoint( .1, .2 );
        double  radius  = 4.5;
        Circle  circle  = new Circle( center, fill, edge, radius );
        
        assertEquals( center, circle.getCenter() );
        assertEquals( radius, circle.getRadius(), .001 );
        assertEquals( edge, circle.getEdgeColor() );
        assertEquals( fill, circle.getFillColor() );
        
        DPoint  exp = new DPoint( -radius, -radius );
        circle = new Circle( null, fill, edge, radius );
        assertEquals( exp, circle.getOrigin() );
        assertEquals( radius, circle.getRadius(), .001 );
        assertEquals( edge, circle.getEdgeColor() );
        assertEquals( fill, circle.getFillColor() );
    }
    
    @Test
    public void testDraw()
    {
        Canvas  canvas  = new Canvas();
        canvas.start();
        canvas.clearShapes();
        
        CircleSpec[]    allSpecs    =
        {
            new CircleSpec( Color.RED, Color.BLUE, 50 ),
            new CircleSpec( null, Color.BLACK, 100 ),
            new CircleSpec( Color.GREEN, null, 75 ),
        };
        
        Circle  refCircle   = new Circle(); // this circle never gets drawn
        for ( CircleSpec spec : allSpecs )
        {
            Rectangle   rect    = spec.getRectangle( refCircle );
            canvas.addShape( rect );
            
            Circle      circle  = spec.getCircle( refCircle );
            refCircle = circle;
            canvas.addShape( circle );
            canvas.repaint();
            ThreadUtils.pause( 1000 );
        }
        
        ThreadUtils.pause( 1500 );
        canvas.clearShapes();
    }

    private class CircleSpec
    {
        private final Color     fill;
        private final Color     edge;
        private final double    radius;
        
        public CircleSpec( Color fill, Color edge, double radius )
        {
            this.fill = fill;
            this.edge = edge;
            this.radius = radius;
        }
        
        public Circle getCircle( Circle refCircle )
        {
            DPoint  oldCenter   = refCircle.getCenter();
            double  oldRadius   = refCircle.getRadius();
            double  xco         = oldCenter.x + oldRadius + radius;
            double  yco         = oldCenter.y + oldRadius + radius;
            DPoint  center      = new DPoint( xco, yco );

            Circle  circle      = new Circle( center, fill, edge, radius );
            return circle;
        }
        
        public Rectangle getRectangle( Circle refCircle )
        {
            double  refWidth    = refCircle.getWidth();
            double  refHeight   = refCircle.getHeight();
            DPoint  refOrigin   = refCircle.getOrigin();
            
            double  side        = 2 * radius;
            double  xco         = refOrigin.x + refWidth;
            double  yco         = refOrigin.y + refHeight;
            DPoint  origin      = new DPoint( xco, yco );
            
            Rectangle   rect    = 
                new Rectangle( origin, null, Color.BLACK, side, side );
            return rect;
        }
    }
}
