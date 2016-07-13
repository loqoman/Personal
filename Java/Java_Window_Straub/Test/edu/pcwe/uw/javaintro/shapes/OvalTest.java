/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import java.awt.Color;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author jack
 */
public class OvalTest
{  
    public OvalTest()
    {
    }

    @Test
    public void testDefaultConstructor()
    {
        Oval    oval    = new Oval();
        assertNull( oval.getOrigin() );
        assertNull( oval.getFillColor() );
        assertNull( oval.getEdgeColor() );
        assertEquals( 0, oval.getWidth(), .001 );
        assertEquals( 0, oval.getHeight(), .001 );
    }

    @Test
    public void testDPointDoubleDoubleConstructor()
    {
        DPoint  origin  = new DPoint( 1, 2 );
        double  width   = 100;
        double  height  = 200;
        Oval    oval    = new Oval( origin, width, height );
        assertEquals( origin, oval.getOrigin() );
        assertNull( oval.getFillColor() );
        assertNull( oval.getEdgeColor() );
        assertEquals( width, oval.getWidth(), .001 );
        assertEquals( height, oval.getHeight(), .001 );
    }
    
    @Test
    public void testDPointColorColorDoubleDoubleConstructor()
    {
        DPoint  origin  = new DPoint( 1, 2 );
        Color   fill    = Color.YELLOW;
        Color   edge    = Color.PINK;
        double  width   = 100;
        double  height  = 200;
        Oval    oval    = new Oval( origin, fill, edge, width, height );
        assertEquals( origin, oval.getOrigin() );
        assertEquals( fill, oval.getFillColor() );
        assertEquals( edge, oval.getEdgeColor() );
        assertEquals( width, oval.getWidth(), .001 );
        assertEquals( height, oval.getHeight(), .001 );
    }
    
    /**
     * Test of draw method, of class Oval.
     */
    @Test
    public void testDraw()
    {
    }
    
}
