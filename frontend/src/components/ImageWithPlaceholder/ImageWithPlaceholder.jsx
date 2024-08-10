import React, { useState } from "react";

const ImageWithPlaceholder = ({ src, placeholder, alt, ...props }) => {
  const [imageLoaded, setImageLoaded] = useState(false);

  return (
    <div style={{ position: "relative", display: "inline-block" }}>
      {!imageLoaded && (
        <img
          src={placeholder}
          alt="Loading..."
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transition: "opacity 0.5s ease",
            opacity: imageLoaded ? 0 : 1,
          }}
        />
      )}

      <img
        src={src}
        alt={alt}
        onLoad={() => setImageLoaded(true)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transition: "opacity 0.5s ease",
          opacity: imageLoaded ? 1 : 0,
        }}
        {...props}
      />
    </div>
  );
};

export default ImageWithPlaceholder;
