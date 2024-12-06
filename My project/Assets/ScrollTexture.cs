using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScrollTexture3 : MonoBehaviour
{
    public float ScrollSpeedX; 
    public float ScrollSpeedY;
    private MeshRenderer meshRenderer;
    
    void Start()
    {
        meshRenderer = GetComponent<MeshRenderer>();
    }

    void Update()
    {
        meshRenderer.material.mainTextureOffset = new Vector2(Time.realtimeSinceStartup * ScrollSpeedX, Time.realtimeSinceStartup * ScrollSpeedY); 
    }
}