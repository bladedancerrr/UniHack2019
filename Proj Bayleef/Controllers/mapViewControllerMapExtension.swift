//
//  mapViewControllerMapExtension.swift
//  Proj Bayleef
//
//  Created by Peteski Shi on 16/3/19.
//  Copyright © 2019 Petech. All rights reserved.
//
import GoogleMaps


extension mapViewController {
    func loadMapView() {
            let camera = GMSCameraPosition.camera(withLatitude: (userLocation?.latitude)!, longitude: (userLocation?.longitude)!, zoom: 10.0)
            let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
            view = mapView
            showMarker(position: camera.target, mapView: mapView)
    }
    
    
    func showMarker(position: CLLocationCoordinate2D, mapView: GMSMapView){
        let marker = GMSMarker()
        marker.position = position
        marker.title = "Palo Alto"
        marker.snippet = "San Francisco"
        marker.map = mapView
    }
}
