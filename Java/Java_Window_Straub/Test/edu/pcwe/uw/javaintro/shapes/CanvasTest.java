/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import edu.pcwe.uw.javaintro.shapes.util.ThreadUtils;
import java.awt.Color;
import static java.awt.Color.BLACK;
import static java.awt.Color.BLUE;
import static java.awt.Color.CYAN;
import static java.awt.Color.GREEN;
import static java.awt.Color.MAGENTA;
import static java.awt.Color.RED;
import java.awt.Graphics2D;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author psp504ap001
 */
public class CanvasTest
{
    public CanvasTest()
    {
    }

    /**
     * Test of draw method, of class Shape.
     */
    @Test
    public void test()
    {
        testAddShape();
        testDraw();
    }

    /**
     * Test of repaint method, of class Canvas.
     */
    @Test
    public void testRepaint()
    {
        System.out.println("repaint");
        Canvas canvas = new Canvas();
        
        DPoint      point   = new DPoint( 100, 100 );
        Rectangle   rect    = 
            new Rectangle( point, Color.BLUE, Color.GREEN, 100, 200 );
        canvas.addShape( rect );
        canvas.repaint();
        
        canvas.close();
        ThreadUtils.pause( 1000 );
    }

    /**
     * Test of start and run methods, of class Canvas.
     */
    @Test
    public void testStartRun()
    {
        System.out.println( "start/run" );
        Canvas canvas = new Canvas();
        canvas.start();
        
        DPoint      point   = new DPoint( 100, 100 );
        Rectangle   rect    = 
            new Rectangle( point, Color.BLUE, Color.GREEN, 100, 200 );
        canvas.addShape( rect );
        canvas.repaint();
        
        ThreadUtils.pause( 1000 );
        canvas.close();
    }

    public void testDraw()
    {
        Canvas  canvas  = new Canvas();
        Shape[] shapes  = 
        {
            new Rectangle( new DPoint( 10, 10 ), BLUE, RED, 50, 40 ),
            new Oval( new DPoint( 110, 10 ), GREEN, CYAN, 80, 100 ),
            new Circle( new DPoint( 200, 200 ), MAGENTA, BLACK, 75 ),
        };
        
        for ( Shape shape : shapes )
        {
            canvas.addShape( shape );
            canvas.repaint();
            ThreadUtils.pause( 500 );
        }
        
        ThreadUtils.pause( 2000 );
    }

    /**
     * Test of add/RemoveShape methods, of class Shape.
     */
    public void testAddShape()
    {
        Canvas  canvas  = new Canvas();
        Shape[] shapes  = { new Rectangle(), new Oval(), new Circle() };
        for ( int inx = 0 ; inx < shapes.length ; ++inx )
        {
            Shape   shape   = shapes[inx];
            canvas.addShape( shape );
            List<Shape> list    = canvas.getShapes();
            
            assertEquals( inx + 1, list.size() );
            assertEquals( shape, list.get( inx ) );
        }
        
        testRemoveShape( canvas, shapes );
    }

    /**
     * Test of removeShape method, of class Shape.
     */
    public void testRemoveShape( Canvas canvas, Shape[] shapes )
    {
        List<Shape> allShapes   =
            new ArrayList<>( Arrays.asList( shapes ) );
        
        while ( !allShapes.isEmpty() )
        {
            int     inx     = (int)(Math.random() * allShapes.size());
            Shape   shape   = allShapes.remove( inx );
            assertNotNull( shape );
            
            assertTrue( canvas.removeShape( shape ) );
            assertFalse( canvas.removeShape( shape ) );
            
            List<Shape> actual  = canvas.getShapes();
            assertEquals( allShapes.size(), actual.size() );
        }
        assertEquals( 0, canvas.getShapes().size() );
    }

    /**
     * Test of setGraphicsCtx method, of class Shape.
     */
//    @Test
//    public void testSetGetGraphicsCtx()
//    {
//        Canvas      canvas  = new Canvas();
//        Graphics2D  gtx     = canvas.getGraphicsCtx();
//        assertNotNull( gtx );
//        
//        Graphics2D  clone   = (Graphics2D)gtx.create();
//        assertNotSame( clone, gtx );
//        
//        canvas.setGraphicsCtx( clone );
//        Graphics2D  actual  = canvas.getGraphicsCtx();
//        assertSame( clone, actual );
//    }

    /**
     * Test of get/setOrigin methods, of class Shape.
     */
    @Test
    public void testGetSetOrigin()
    {
        Shape   shape   = new SimpleShape();
        DPoint  exp     = new DPoint( 1, 2 );
        shape.setOrigin( exp );
        
        DPoint  act     = shape.getOrigin();
        assertEquals( exp, act );
    }

    /**
     * Test of get/setFillColor method, of class Shape.
     */
    @Test
    public void testGetFillColor()
    {
        Shape   shape   = new SimpleShape();
        Color   exp     = Color.RED;
        shape.setFillColor( exp );
        
        Color   act = shape.getFillColor();
        assertEquals( exp, act );
    }

    
    /**
     * Test of get/setEdgeColor method, of class Shape.
     */
    @Test
    public void testGetSetEdgeColor()
    {
        Shape   shape   = new SimpleShape();
        Color   exp     = Color.RED;
        shape.setEdgeColor( exp );
        
        Color   act = shape.getEdgeColor();
        assertEquals( exp, act );
    }

    /**
     * Test of getShapes method, of class Shape.
     */
    @Test
    public void testGetShapes()
    {
        List<Shape> testBucket  = new ArrayList<>();
        Canvas      canvas      = new Canvas();
        canvas.clearShapes();
        int         testCount   = 10;
        for ( int inx = 0 ; inx < testCount ; ++inx )
        {
            SimpleShape shape   = new SimpleShape( inx );
            canvas.addShape( shape );
            testBucket.add( shape );
        }
        
        List<Shape> shapes  = canvas.getShapes();
        assertEquals( testBucket.size(), shapes.size() );
        
        for ( int inx = 0 ; inx < testCount ; ++inx )
            assertEquals( testBucket.get( inx ), shapes.get( inx ) );
    }
    
    @Test
    public void testClearShapes()
    {
        Canvas  canvas  = new Canvas();
        int     count   = 3;
        canvas.clearShapes();
        for ( int inx = 0 ; inx < count ; ++inx )
            canvas.addShape( new SimpleShape() );
        
        int size    = canvas.getShapes().size();
        assertEquals( count, size );
        canvas.clearShapes();
        size = canvas.getShapes().size();
        assertEquals( 0, size );        
    }

    /**
     * Test of minimize and restore methods, of class Canvas.
     */
    @Test
    public void testMinimizeRestore()
    {
        System.out.println("minimize/restore");
        Canvas canvas = new Canvas();
        
        DPoint      point   = new DPoint( 100, 100 );
        Rectangle   rect    = 
            new Rectangle( point, Color.BLUE, Color.GREEN, 100, 200 );
        canvas.addShape( rect );
        canvas.repaint();
        
        canvas.minimize();
        ThreadUtils.pause( 500 );
        canvas.restore();
        ThreadUtils.pause( 500 );
        canvas.close();
    }
    
    @Test
    public void testClose()
    {
        System.out.println("close");
        Canvas canvas = new Canvas();
        canvas.close();
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
