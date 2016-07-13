/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes;

import java.awt.Color;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;
/**
 * This class provides a simple window for doing graphical exercises, 
 * such as drawing polygons and circles. If you use this class you
 * will have to learn to use the{@link java.awt.Graphics2D} class.
 * 
 * @see java.awt.Graphics2D
 * @see Shape
 * @author jack
 */
public class Canvas
    implements Runnable
{
    /** The default width of the canvas.*/
    public static final int DEFAULT_WIDTH   = 500;
    /** The default height of the canvas. */
    public static final int DEFAULT_HEIGHT  = 500;
    /**
     * For testing only. Indicates to the start() method
     * that no special test logic is to take place.
     * @see #start
     */
    protected static final int  THROW_NONE                  = 0;
    /**
     * For testing only. Indicates to the start() method
     * that no special test logic is to take place. That
     * an InvocationTargetException is to be simulated.
     */
    protected static final int  THROW_INVOCATION_EXCEPTION  = 1;
    /**
     * For testing only. Indicates to the start() method
     * that no special test logic is to take place. That
     * an InterruptedException is to be simulated.
     */
    protected static final int  THROW_INTERRUPTED_EXCEPTION = 2;
    
    private final InternalFrame frame       = new InternalFrame( "Drawing Board" );
    private final List<Shape>   allShapes   = new ArrayList<>();
    private Graphics2D          graphicsCtx;
    private final Dimension     size;
    
    private int throwFlag   = THROW_NONE;
    /**
     * Default constructor. The width and height of the Canvas
     * are set to DEFAULT_WIDTH and DEFAULT_HEIGHT, respectively.
     */
    public Canvas()
    {
        this( DEFAULT_WIDTH, DEFAULT_HEIGHT );
    }
    /**
     * Constructor to create a canvas with the given width and height.
     * 
     * @param width     The given width.
     * @param height    The given height.
     */
    public Canvas( int width, int height )
    {
        size = new Dimension( width, height );
    }
    /**
     * Causes the canvas to be repainted. This is necessary any time
     * you change the state of the Canvas, for example after you add
     * a new shape.
     * 
     * @see Shape#addShape(edu.pcwe.uw.javaintro.shapes.Shape) 
     * @see Shape#removeShape(edu.pcwe.uw.javaintro.shapes.Shape) 
     * @see Shape#redraw() 
     */
    public void repaint()
    {
        frame.repaint();
    }
    
    /**
     * Starts the GUI in a new thread. Blocks until the GUI is fully built
     * and ready to use.
     */
    public void start()
    {
        try //Dont know what the hell this is???
        {
            SwingUtilities.invokeAndWait( this );
        }
        catch ( InvocationTargetException | InterruptedException exc )
        {
            // If exception is due to testing throw an Error; otherwise exit.
            if ( throwFlag == THROW_NONE )
            {
                exc.printStackTrace();
                System.exit( 1 );
            }
            else
                throw new Error();
        }
    }
    /**
     * Builds the Canvas GUI; required by interface Runnable.
     */
    @Override
    public void run()
    {
        Container   pane    = frame.getContentPane();

        pane.setPreferredSize( size );
        pane.setBackground( Color.WHITE );

        frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE ); //This defaults to
        frame.pack();
        frame.setVisible( true );

        graphicsCtx = (Graphics2D)pane.getGraphics();
    }
    /**
     * Closes the GUI, releasing all associated resources.
     */
    public void close(){
        frame.setVisible( false );
        frame.dispose();
    }
    /**
     * Places the canvas GUI in the minimized state.
     */
    public void minimize(){
        frame.setState( JFrame.ICONIFIED );
    }
    /**
     * Places the canvas GUI in the restored state.
     */
    public void restore(){
        frame.setState( JFrame.NORMAL );
    }
    /**
     * Adds a Shape to the draw queue. Merely adding a Shape to the queue
     * does not mean it is drawn; to draw the Shape immediately call
     * Canvas.repaint(). All shapes in the queue will be redrawn whenever all
     * or part of a Canvas is exposed.
     * 
     * @param shape The shape to add to the queue.
     * 
     * @see #removeShape( Shape )
     * @see #clearShapes() 
     * @see #repaint() 
     */
    public void addShape( Shape shape ){
        allShapes.add( shape );
    }
    /**
     * Removes a Shape from the queue. The drawing of the Shape on the
     * Canvas will not be immediately removed; to remove the Shape from
     * the Canvas immediately, call Canvas.repaint().
     * 
     * @param shape The shape to remove.
     * 
     * @return true if <em>shape</em> is found in the queue and removed;
     *         false if <em>shape</em> could not be found in the queue.
     * 
     * @see #removeShape( Shape )
     * @see #clearShapes() 
     * @see #repaint() 
     */
    public boolean removeShape( Shape shape ){
        boolean rval    = allShapes.remove( shape );
        return rval;
    }
    /**
     * Removes all Shapes from the draw queue.
     * 
     * @see #addShape( Shape )
     * @see #removeShape( Shape )
    */
    public void clearShapes(){
        allShapes.clear();
    }
    /**
     * Gets a read-only list of all the Shapes in the draw queue.
     * 
     * @return A read-only list of all the Shapes in the draw queue.
     */
    public List<Shape> getShapes(){
        List<Shape> list    = Collections.unmodifiableList( allShapes );
        return list;
    }
        
    /**
     *  Redraws all the Shapes in the draw queue.
     */
    public void redraw(){
        for ( Shape shape : allShapes )
            shape.draw( graphicsCtx );
    }
    private class InternalFrame extends JFrame{
        public InternalFrame( String title ){
            super( title );
        }
        
        @Override
        public void paint( Graphics graphics ){
            super.paint( graphics );
            graphics.setClip( 0, 0, getWidth(), getHeight() );
            redraw();
        }
    }
}
