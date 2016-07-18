/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import edu.pcwe.uw.javaintro.shapes.util.ThreadUtils;
import java.awt.Color;
import java.lang.reflect.InvocationTargetException;
import javax.swing.SwingUtilities;

/**
 *
 * @author jack
 */
public class Orig
{
    public static void main( String[] args )
    {
        System.out.println( "main" );
        Canvas  canvas  = new Canvas();
        try
        {
            SwingUtilities.invokeAndWait( canvas );
        }
        catch ( InvocationTargetException | InterruptedException exc )
        {
            exc.printStackTrace();
            System.exit( 1 );
        }
        
        DPoint      orig    = new DPoint( 100, 100 );
        Rectangle   rect    = 
            new Rectangle( orig, Color.BLUE, Color.RED, 100, 200 );
        canvas.addShape( rect );
        canvas.redraw();
        canvas.repaint();
        ThreadUtils.pause( 1000 );
        
        orig = new DPoint( 200, 200 );
        rect = new Rectangle( orig, Color.GREEN, Color.BLUE, 50, 100 );
        canvas.addShape( rect );
        canvas.redraw();
        ThreadUtils.pause( 1000 );
        
        orig = new DPoint( 300, 300 );
        rect = new Rectangle( orig, null, Color.BLACK, 50, 100 );
        canvas.addShape( rect );
        canvas.redraw();
        ThreadUtils.pause( 1000 );
        
        orig = new DPoint( 400, 400 );
        rect = new Rectangle( orig, Color.CYAN, null, 50, 100 );
        canvas.addShape( rect );
        canvas.redraw();
        ThreadUtils.pause( 1000 );
    }
}
