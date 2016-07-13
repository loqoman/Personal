/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import java.awt.Point;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author jack
 */
public class DPointTest
{
    /*
     * DPoint pairs for equality testing. The two components of each pair
     * are always equal
    */
    DPoint[][]  testPoints  = 
    {
        { new DPoint( 1, 2 ), new DPoint( 1, 2 ) },
        { new DPoint( 2, 3 ), new DPoint( 2, 3 ) },
        { new DPoint( 3, 4 ), new DPoint( 3, 4 ) },
    };
    
    /**
     * Test of getPoint method, of class DPoint.
     */
    @Test
    public void testGetPoint()
    {
        for ( int inx = 0 ; inx < 10 ; ++inx )
        {
            DPoint  point1      = new DPoint( inx, 2 * inx );
            Point   expPoint1   = new Point( inx, 2 * inx );
            Point   actPoint1   = point1.getPoint();
            assertEquals( expPoint1, actPoint1 );
            
            DPoint  point2      = new DPoint( inx + .1, 2 * inx + .1 );
            Point   expPoint2   = new Point( inx, 2 * inx );
            Point   actPoint2   = point2.getPoint();
            assertEquals( expPoint2, actPoint2 );
            
            DPoint  point3      = new DPoint( inx + .5, 2 * inx + .5 );
            Point   expPoint3   = new Point( inx + 1, 2 * inx + 1 );
            Point   actPoint3   = point3.getPoint();
            assertEquals( expPoint3, actPoint3 );
            
            DPoint  point4      = new DPoint( inx + .6, 2 * inx + .6 );
            Point   expPoint4   = new Point( inx + 1, 2 * inx + 1 );
            Point   actPoint4   = point4.getPoint();
            assertEquals( expPoint4, actPoint4 );
        }
    }
    
    /**
     * Test of equals method, of class DPoint.
     */
    @Test
    public void testEquals()
    {
        for ( int inx = 0 ; inx < testPoints.length ; ++inx )
        {
            DPoint  point0      = testPoints[inx][0];
            DPoint  point1      = testPoints[inx][1];
            DPoint  nePoint0    = new DPoint( point0.x + 1, .1 );
            DPoint  nePoint1    = new DPoint( point0.x + 1, point0.y );
            DPoint  nePoint2    = new DPoint( point0.x, point0.y + 1 );
            
            assertTrue( point0.equals( point0 ) );
            assertTrue( point1.equals( point1 ) );
            assertTrue( point0.equals( point1 ) );
            assertTrue( point1.equals( point0 ) );
            assertFalse( point0.equals( null ) );
            assertFalse( point1.equals( null ) );
            assertFalse( point0.equals( nePoint0 ) );
            assertFalse( point1.equals( nePoint0 ) );
            assertFalse( point0.equals( nePoint1 ) );
            assertFalse( point1.equals( nePoint1 ) );
            assertFalse( point0.equals( nePoint2 ) );
            assertFalse( point1.equals( nePoint2 ) );
            assertFalse( point1.equals( new Object() ) );
        }
    }
    
    /**
     * Test of getPoint hashCode, of class DPoint.
     */
    @Test
    public void testHashCode()
    {
        for ( int inx = 0 ; inx < testPoints.length ; ++inx )
        {
            DPoint  point0  = testPoints[inx][0];
            DPoint  point1  = testPoints[inx][1];
            
            assertEquals( point0.hashCode(), point1.hashCode() );
        }
    }

    /**
     * Test default constructor of class DPoint.
     */
    @Test
    public void testDefaultConstructor()
    {
        DPoint  point   = new DPoint();
        assertEquals( 0, point.x, .0001 );
        assertEquals( 0, point.y, .0001 );
    }

    /**
     * Test default constructor of class DPoint.
     */
    @Test
    public void testCopyConstructor()
    {
        DPoint  point   = new DPoint( 5, 10 );
        DPoint  copy    = new DPoint( point );
        assertEquals( 5, copy.x, .0001 );
        assertEquals( 10, copy.y, .0001 );
        assertEquals( point, copy );
    }

    /**
     * Test constructor( double, double ) of class DPoint.
     */
    @Test
    public void testConstructor()
    {
        double  xco     = 1.5;
        double  yco     = 2.3;
        DPoint  point   = new DPoint( xco, yco );
        assertEquals( xco, point.x, .0001 );
        assertEquals( yco, point.y, .0001 );
    }
    
    /**
     * Test of getDistanceTo method, of class DPoint.
     */
    @Test
    public void testGetDistanceTo()
    {
        DistanceSpec[]  dSpecs  =
        {
            new DistanceSpec( 0, 0, 0, 0, 0 ),
            new DistanceSpec( 0, 0, 0, 5, 5 ),
            new DistanceSpec( 0, 0, 0, -5, 5 ),
            new DistanceSpec( 0, 0, 5, 0, 5 ),
            new DistanceSpec( 0, 0, -5, 0, 5 ),
            new DistanceSpec( 0, 0, 3, 4, 5 ),
            
            new DistanceSpec( 1, 2, 1, 2, 0 ),
            new DistanceSpec( 1, 2, 1, 7, 5 ),
            new DistanceSpec( 1, 2, 6, 2, 5 ),
            new DistanceSpec( 1, 2, 4, 6, 5 ),
        };
        
        for ( DistanceSpec spec : dSpecs )
            spec.test();
    }

    /**
     * Test of toString method, of class DPoint.
     */
    @Test
    public void testToString()
    {
    }
    
    private class DistanceSpec
    {
        private final DPoint    point1;
        private final DPoint    point2;
        private final double    expected;
        
        public DistanceSpec( DPoint point1, DPoint point2, double distance )
        {
            this.point1 = point1;
            this.point2 = point2;
            this.expected = distance;
        }
        
        public DistanceSpec(
            double xco1,
            double yco1, 
            double xco2, 
            double yco2, 
            double distance 
        )
        {
            this(
                new DPoint( xco1, yco1 ),
                new DPoint( xco2, yco2 ),
                distance
            );
        }
        
        public void test()
        {
            String  msg;
            
            test( point1, point2, expected );
            test( point2, point1, expected );
            test( point1, point1, 0 );
            test( point2, point2, 0 );
        }
        
        private void test( DPoint point1, DPoint point2, double distance )
        {
            StringBuilder   bldr    = new StringBuilder( "Testing " );
            bldr.append( point1 ).append( ", " ).append( point2 );
            bldr.append( ": " ).append( distance );
            System.out.println( bldr );
            
            double  actual  = point1.getDistanceTo( point2 );
            assertEquals( distance, actual, .005 );
        }
    }
}
