/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.pcwe.uw.javaintro.shapes.util;

/**
 *
 * @author jack
 */
public class ThreadUtils
{
    public static void pause( long millis )
    {
        try
        {
            Thread.sleep( millis );
        }
        catch ( InterruptedException exc )
        {
        }
    }
}
