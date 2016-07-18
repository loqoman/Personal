/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import edu.pcwe.uw.javaintro.shapes.util.ThreadUtils;
import java.awt.Graphics2D;
import java.util.List;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Arrays;
import javax.swing.SwingUtilities;
import org.junit.Test;

import static org.junit.Assert.*;
import static java.awt.Color.*;
import java.awt.Color;

/**
 *
 * @author jack
 */
public class ShapeTest
{
    private final Canvas    canvas  = new Canvas();
    
    public ShapeTest()
    {
        try
        {
            SwingUtilities.invokeAndWait( canvas );
        }
        catch ( InvocationTargetException | InterruptedException exc )
        {
            exc.printStackTrace();
            System.exit( 1 );
        }      
    }
    
    @Test
    public void testDefaultConstructor()
    {
        Shape   shape   = new SimpleShape();
        assertNull( shape.getOrigin() );
        assertNull( shape.getFillColor() );
        assertNull( shape.getEdgeColor() );
    }
    
    @Test
    public void testDPointConstructor()
    {
        DPoint  origin  = new DPoint( 1, 2 );
        Shape   shape   = new SimpleShape( origin );
        assertEquals( origin, shape.getOrigin() );
        assertNull( shape.getFillColor() );
        assertNull( shape.getEdgeColor() );
    }
    
    @Test
    public void testDPointColorColorConstructor()
    {
        DPoint  origin  = new DPoint( 1, 2 );
        Color   fill    = Color.RED;
        Color   edge    = Color.YELLOW;
        Shape   shape   = new SimpleShape( origin, fill, edge );
        assertEquals( origin, shape.getOrigin() );
        assertEquals( fill, shape.getFillColor() );
        assertEquals( edge, shape.getEdgeColor() );
    }
    
    private class SimpleShape extends Shape
    {
        private final int fingerPrint;
        
        public SimpleShape()
        {
            this( 0 );
        }
        
        public SimpleShape( int fingerPrint )
        {
            this.fingerPrint = fingerPrint;
        }
        
        public SimpleShape( DPoint origin )
        {
            super( origin );
            fingerPrint = 0;
        }
        
        public SimpleShape( DPoint origin, Color fill, Color edge )
        {
            super( origin, fill, edge );
            fingerPrint = 0;
        }
        
        public int getFingerPrint()
        {
            return fingerPrint;
        }
        
        // required by interface; not used
        public void draw( Graphics2D gtx )
        {
        }
        
        public int hashCode()
        {
            int xier    = 101;
            int hash    = fingerPrint * xier;
            return hash;
        }
        
        public boolean equals( Object obj )
        {
            boolean rcode   = false;
            
            if ( this == obj )
                rcode = true;
            else if ( obj!= null && obj instanceof SimpleShape )
                rcode = this.fingerPrint == ((SimpleShape)obj).fingerPrint;
            
            return rcode;
        }
    }
}
