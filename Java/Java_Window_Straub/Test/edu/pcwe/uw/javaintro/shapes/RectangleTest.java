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
public class RectangleTest
{
    
    public RectangleTest()
    {
    }

    /**
     * Test of default constructor, of class Rectangle.
     */
    @Test
    public void testDefaultConstructor()
    {
        Rectangle   rect    = new Rectangle();
        assertNull( rect.getOrigin() );
        assertNull( rect.getEdgeColor() );
        assertNull( rect.getFillColor() );
        assertEquals( 0, rect.getWidth(), .001 );
        assertEquals( 0, rect.getHeight(), .001 );
    }

    /**
     * Test of constructor, of class Rectangle.
     */
    @Test
    public void testDPointDoubleDoubleConstructor()
    {
        double      width   = 5.5;
        double      height  = 10.1;
        DPoint      origin  = new DPoint( 1.1, -2.2 );
        Rectangle   rect    = new Rectangle( origin, width, height );
        assertEquals( origin, rect.getOrigin() );
        assertNull( rect.getEdgeColor() );
        assertNull( rect.getFillColor() );
        assertEquals( width, rect.getWidth(), .001 );
        assertEquals( height, rect.getHeight(), .001 );
    }

    /**
     * Test of constructor, of class Rectangle.
     */
    @Test
    public void testDPointColorColorDoubleDoubleConstructor()
    {
        double      width   = 5.5;
        double      height  = 10.1;
        Color       fill    = Color.RED;
        Color       edge    = Color.BLUE;
        DPoint      origin  = new DPoint( 1.1, -2.2 );
        Rectangle   rect    =
            new Rectangle( origin, fill, edge, width, height );
        assertEquals( origin, rect.getOrigin() );
        assertEquals( edge, rect.getEdgeColor() );
        assertEquals( fill, rect.getFillColor() );
        assertEquals( width, rect.getWidth(), .001 );
        assertEquals( height, rect.getHeight(), .001 );
    }

    /**
     * Test of getWidth method, of class Rectangle.
     */
    @Test
    public void testGetSetWidthHeight()
    {
        DPoint      origin      = new DPoint( -5, -5 );
        double      width       = 100;
        double      newWidth    = 200;
        double      height      = 50;
        double      newHeight   = 100;
        
        Rectangle   rect        = new Rectangle( origin, width, height );        
        assertEquals( width, rect.getWidth(), .001 );
        assertEquals( height, rect.getHeight(), .001 );
        
        rect.setWidth( newWidth );
        rect.setHeight( newHeight );
        assertEquals( newWidth, rect.getWidth(), .001 );
        assertEquals( newHeight, rect.getHeight(), .001 );
    }

    /**
     * Test of getIntWidth method, of class Rectangle.
     */
    @Test
    public void testGetIntWidthHeight()
    {
        double[]    testVals    = 
            { .1, .5, .6, 1.1, 1.5, 1.6, -1.1, -1.5, 1.6 };
        DPoint  origin  = new DPoint();
        Rectangle   rect    = new Rectangle( origin, 0, 0 );
        
        assertEquals( 0, rect.getIntWidth() );
        assertEquals( 0, rect.getIntHeight() );
        
        for ( double val : testVals )
        {
            rect.setWidth( val );
            int exp = (int)Math.round( val );
            assertEquals( exp, rect.getIntWidth() );
        }
        
        for ( double val : testVals )
        {
            rect.setHeight( val );
            int exp = (int)Math.round( val );
            assertEquals( exp, rect.getIntHeight() );
        }
    }

    /**
     * Test of draw method, of class Rectangle.
     */
    @Test
    public void testDraw()
    {
        Canvas      canvas      = new Canvas();
        canvas.start();
        
        RectSpec[]  allSpecs    =
        {
            new RectSpec( Color.BLUE, Color.RED, 150, 250 ),
            new RectSpec( Color.RED, null, 50, 100 ),
            new RectSpec( null, Color.BLUE, 100, 200 ),
        };
        
        /*   // this rectangle never gets painted */
        DPoint      origin  = new DPoint( 0, 0 );
        Rectangle   refRect = new Rectangle( origin, 0, 0 );
        for ( RectSpec spec : allSpecs )
        {
            Rectangle   rect    = spec.getRect( refRect );
            canvas.addShape( rect );
            canvas.repaint();
            refRect = rect;
            ThreadUtils.pause( 1000 );
        }
        
        canvas.minimize();
        ThreadUtils.pause( 1000 );
        canvas.restore();
        
        ThreadUtils.pause( 1000 );
    }
    
    private class RectSpec
    {
        private final Color     fill;
        private final Color     edge;
        private final double    width;
        private final double    height;
        
        public RectSpec( Color fill, Color edge, double width, double height )
        {
            this.fill = fill;
            this.edge = edge;
            this.width = width;
            this.height = height;
        }
        
        public Rectangle getRect( Rectangle refRect )
        {
            DPoint  refOrigin   = refRect.getOrigin();
            double  refX        = refOrigin.x;
            double  refY        = refOrigin.y;
            double  refWidth    = refRect.getWidth();
            double  refHeight   = refRect.getHeight();
            
            double      xco     = refX + refWidth;
            double      yco     = refY + refHeight;
            DPoint      origin  = new DPoint( xco, yco );
            Rectangle   rect    = 
                new Rectangle( origin, fill, edge, width, height );
            
            return rect;
        }
    }
}
